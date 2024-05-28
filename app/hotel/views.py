from django.http import JsonResponse
from django.shortcuts import render
from .models import Hotel, HotelSerializer, HotelsApi, RoomSerializer, RoomsApi, init_hotel
import requests

# html views
def hotel_view(request, hotel_id):
    # in the test we always return the same hotel
    hotel = Hotel.objects.first() 
    if hotel == None:
        print("init_hotel")
        hotel = init_hotel(None)
    else:
        print("hotel loaded from db")
    info = hotel.info

    return render(request, 'hotel/hotel.html', {
        'name' : info['name'],
        'images' : info['images'],
        'accommodation_type_code' : info['accommodation_type_code'],
        'full_address' : info['full_address'],
        'city' : info['city'],
        'longitude' : info['longitude'],
        'latitude' : info['latitude'],
        'neighbourhood' : '',
        'points_of_interest' : '',
        'nearby_airports' : '',

        'guest_rating_overall' : info['additional_info']['guest_rating_overall'],
        'guest_rating_cleanliness' : info['additional_info']['guest_rating_cleanliness'],
        'guest_rating_service' : info['additional_info']['guest_rating_service'],
        'guest_rating_comfort' : info['additional_info']['guest_rating_comfort'],
        }
    )


# api views

# /api/hotels/{hotel_id}
def hotel_json(request, hotel_id):
    # in this test always return the same hotel
    base_info = HotelsApi.queryset.first()
    result = HotelSerializer(base_info, many=False).data

    # external data source
    url = "https://www.mobytrip.com/apis/hotels/65741/?check_in=2024-05-19&check_out=2024-05-20&rooms=1&from_landing=&currency=USD&room0_adults=2&room0_children=0"
    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.json()
        result = {**result, **response_json}
    else:
        print("Error: External data request failed, defaulting to internal data")
    return JsonResponse(result, safe=False)

# /api/rooms/{hotel_id}
def room_json(request, hotel_id):
    # in this test always return rooms for the same hotel
    the_hotel = HotelsApi.queryset.first()
    rooms = RoomsApi.queryset.filter(hotel=the_hotel)
    print("rooms count: ", rooms.count())
    serializer = RoomSerializer(rooms, many=True)
    return JsonResponse(serializer.data, safe=False)
