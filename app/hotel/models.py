from django.db import models
from rest_framework import serializers, viewsets
from django.dispatch import receiver

class Hotel(models.Model):
    name = models.CharField(max_length = 100)
    info = models.JSONField( default=None, blank=True, null=True)

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete = models.CASCADE)
    code = models.CharField(max_length = 20)
    name = models.CharField(max_length = 100)
    description = models.TextField()

class Rate(models.Model):
    room = models.ForeignKey(Room, related_name='rates', on_delete = models.CASCADE)
    rooms = models.IntegerField()
    adults = models.IntegerField()
    children = models.IntegerField()
    baseRate = models.CharField(max_length = 20)
    tax = models.CharField(max_length = 20)
    chargeAmount = models.CharField(max_length = 20)
    otherFees = models.CharField(max_length = 20)
    strikeThroughPrice = models.CharField(max_length = 20)

class RateSerializer(serializers.ModelSerializer):        
    class Meta:
        model = Rate
        fields = ['rooms', 'adults', 'children', 'baseRate', 'tax', 'chargeAmount', 'otherFees', 'strikeThroughPrice']

class RoomSerializer(serializers.ModelSerializer):
    rates = RateSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ['code', 'name', 'description', 'rates']

class HotelSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True, read_only=True)
    class Meta:
        model = Hotel
        fields = ['info', 'name', 'rooms']

class HotelsApi(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class RoomsApi(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RatesApi(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

#@receiver(post_migrate)
def init_hotel(sender, **kwargs):
    #sender, app, created_models, verbosity, 
    print("==========> init started")
    null = None
    true = True
    false = False
    j = {
        "code": 65741,
        "name": "Hyatt Regency Chicago",
        "description": "Off the banks of the Chicago River, this luxurious hotel is conveniently located within 5 minutes' walk of the Magnificent Mile and Millennium Park. As the largest hotel in Chicago, this hotel features numerous of on-site dining options, free WiFi, and a 24-hour fitness center and spa. Each environmentally-friendly room at Chicago Hyatt Regency includes a 37-inch flat-screen TV and an iPod docking station. A desk and seating area are also provided in every room. The hotel offers a wide array of services on site, including car rental, a concierge staff, a babies travel lite program, 24-hour in-room dining, and ticket services. Laundry and dry cleaning services are also available on site. Stetsons Modern Steak + Sushi serves fine chops and seafood in an elegant atmosphere. Market Chicago, open 24-hours a day, features Starbucks coffee, sandwiches and breakfast items. BIG Bar features views of the city and signature cocktails. American Craft Kitchen and Bar is open for lunch and dinner and serves sandwiches and salads. Chicago Hyatt Regency is a 10 minutes' walk from the Chicago Theater District. The Art Institute of Chicago and Museum of Science and Industry are within 1 mile.",
        "city": "CHICAGO",
        "address": "On The Riverwalk",
        "longitude": -87.622207641602,
        "latitude": 41.888000488281,
        "stars": 4,
        "accommodation_type_code": "Hotel",
        "images": [
            {
            "internal_sort_order": 1,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/454695817.jpg?k=cd83e894ab90bbcbd9dd15ba3832a27e7cccf9c2029df1c52039ae785b80d39f&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 2,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312169.jpg?k=0e57ed7186bb257c637745060899d08cbe927419deedcc66388f617cbf8077b2&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 3,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312186.jpg?k=ed20a45e775ad0052df6bc06eee8b6a99f70605a568625073aaeab10103e7ef1&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 4,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312191.jpg?k=2305f69d9061e8d042f5dcc917d68ee6d763c6ba4cf116c5442187567fcf1010&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 5,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312190.jpg?k=af19dfb49070b5f7fcd6ea044b393c100edacfb1ec9da1ad9d4e5860efb8b442&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 6,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312194.jpg?k=66b200c50e9a518cd62c956ba1bbc64677005ee827522e766178a761514b4ea7&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 7,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312197.jpg?k=0ee43f07fbece278b10481ab27e47beb7bfd278cdc5ef26a10379236e3b1c029&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 8,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312196.jpg?k=37f89d19d9c9c1b8d47f4995532e7db0ed0a70bc918533e287b806ca15e6c180&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 9,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312202.jpg?k=6a7d957674f27e0c74b48a6c21e8f756623a0b4b2b9f122444d159931d169cd5&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 10,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312206.jpg?k=3f70e18aed26c437bf17d3709149ae0e20897da84c68b7b376267f31b7ad3c3e&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 11,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312204.jpg?k=e89e24ed2623ae0bcc7a2c6f54e8011ca215e221cb9d7ee5a1028a9f9876f1c0&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 12,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312207.jpg?k=740904bd6e86a31fa9206d44f04d62035bb06b6848051fd8f40d732136c48d7d&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 13,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312209.jpg?k=e336bfbccdc94fc5ca94da6d6e386ef56107d054370b43f0c2049f5fe24f6c1f&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 14,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312211.jpg?k=3bf826bbb738e482e403a53a3889701b8b7309aa588d567b50ca3a1aa3bcf74d&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 15,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312212.jpg?k=8af554bd0e0e78329dd02cd42b7456997dafc2930bec016b63d6ca69c6faab78&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 16,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312214.jpg?k=409a080ff1579885c623e5f8d188f7efd70cf99ad299236aaad6af067cf7fc0b&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 17,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312216.jpg?k=18702733f3710490ca78f272c2bac4a632af49230a6bc2e48677b9e6f548d7a7&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 18,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312217.jpg?k=cace4d1fb18b00d249796ba6fdb0e3463e78668c752570d4aa11956e73564aeb&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 19,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312225.jpg?k=e4be46a209c9986c713e8bb3a9dfa591e2be1c2c0ec02a9ac34c47cafca0aa8e&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 20,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312224.jpg?k=72aea1d01efea635609b90d7bbbd4e816250884898701a2773832c4306b8c290&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 21,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312226.jpg?k=17657934c5bf25aba52a49775abf6d07df320413875261590313bb5fc3222cc2&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 22,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312233.jpg?k=b50d26237c34ec547d48d3553790424afe0872bc8537c28a9cc67c08aa000324&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 23,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312234.jpg?k=3801735a3509a9685a09c2ed06f2636c384f9c65880c999008f80d5490f69da8&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 24,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312235.jpg?k=833643a1097abab8ec7724fe6e8a31917219518eb7676358c345c12a62c1ce16&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 25,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312242.jpg?k=624767574b9590517c1f21379c8c8597f0aaaa2f66069a6a313466686b8c5361&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 26,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312241.jpg?k=a5033afccfdfa124d27f48b0d7d464d7b04c43672c8be119f8bb96f32084b137&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 27,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312243.jpg?k=9d407cdf84056acfe0a952f82181b524ec68f35782f5e23cf7e6ca8b92a68783&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 28,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312246.jpg?k=307b3045e6f07dbf7ab847189396adc03a3b6c8e21a22ebf17ffc3b3b699a30f&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 29,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312247.jpg?k=e0a6b2b81c8c24e36454cc5d050115bff8e7c0d7ed3a0549dd5bc9d94685250f&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 30,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312249.jpg?k=af9851c0d316035c1c6ed2c1cd6fa5906ba8bf5bb62358e751986b3ed7e1ce1c&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 31,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312261.jpg?k=3a9f754f9e6e626d72089ec23e4c4a02dacaef52fdfb67f5ff55d73d1498c8ba&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 32,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312256.jpg?k=e72b4fc9f0b14250f6e4e0f9da7d2eb11d63da88fbfa859bc1a5b6ce42c74521&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 33,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312259.jpg?k=cf5e6b0618cca36c745ef418f0964ad88c3b9b25f0568be1a8ae7d06581947b3&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 34,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312267.jpg?k=1d41ce4bf94ef62cc240100356dc558c017b1b2cbad2fc1f7a00353a1d1d0757&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 35,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312268.jpg?k=e3fba0a25ada7cf659d1cfdb10c869481f54a999710668257d513be66440cd9c&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 36,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312272.jpg?k=df807d32c246c07f613a6d122e4cc3e13f53de67177fb3b5a219cb70ae872c22&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 37,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312282.jpg?k=3aa5420a2643905f7aeb1f0fe04dfe3cb931d33b12b32b0932a719e88ccb5c28&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 38,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312281.jpg?k=f4ac9baf2a6f52162a3f17cedd5a7284e26db49063e0d1d4162b6b3135ff40b8&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 39,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312285.jpg?k=e059246dfbde496806a2a0a051c26c879c1ec458c0acf462c77cfc0e4dcce747&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 40,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312292.jpg?k=04a76927ebd132f6cc6ad771138b496912becdbe1b1cc555c7d9ccf08516f155&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 41,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312294.jpg?k=be903398ebf1261b39334e14b8085ec2095a811bfbcaaafb259e81c0191e0e97&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 42,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312295.jpg?k=ec1db00ed18f3058a4a8c8f8b41743f5e3404383375a4c6f978565bd81a0f2d5&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 43,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312304.jpg?k=988c2da876942b74dfcc8524d88bc3996eb1626844aa96fc89431fb0366de52f&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 44,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312306.jpg?k=0ba7940ec15f19467ec4eb7ed61521fba23bfa8847b5ac655bab08657b2e659c&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 45,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312307.jpg?k=379d825f23f2eaf08021b17e8ea3547710598f424ae283c91b3d8daf3e964254&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 46,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312314.jpg?k=8317055d1f94cc3aafdc1827f79b0b9fe29009cee649f9853fe42e619cbae89f&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 47,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312316.jpg?k=0f3a0f2bc98a499dd2ecb8492c6613d23e0796671a5d1d5ab37adb936074370e&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 48,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312315.jpg?k=ce2f56e65099dc05ca041787f2ff2c3a5f45ee03c56b730c283a0ccdb95e8cca&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 49,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312328.jpg?k=37d0bb9132594797996d5879cd62ec1ac3443d0ed6f712b96e1af5822d67d1a8&o=",
            "provider": "PPN"
            },
            {
            "internal_sort_order": 50,
            "description": null,
            "thumbnail_url": null,
            "fullsize_url": "https://q-xx.bstatic.com/xdata/images/hotel/max500/516312321.jpg?k=ff12f7cf05aae774b88b0c6c3d835a99b3e713cff0b294334ec968fa01ced60d&o=",
            "provider": "PPN"
            }
        ],
        "hotel_issues": [
            {
            "alternative": false,
            "issue": {
                "code": "COVID",
                "description": "Due to the pandemic, many accommodation and service providers may implement processes and policies to help protect the safety of all of us. This may result in the unavailability or changes in certain services and amenities that are normally available from them.More info here https://cutt.ly/MT8BJcv",
                "name": "Due to the pandemic, many accommodation and service providers may implement processes and policies to help protect the safety of all of us. This may result in the unavailability or changes in certain services and amenities that are normally available from them.More info here https://cutt.ly/MT8BJcv",
                "type": "COVID"
            },
            "date_from": "2020-05-15T00:00:00Z",
            "date_to": "2023-06-30T00:00:00Z"
            }
        ],
        "facilities": [
            {
            "facility__group_code": 10,
            "facility": "10_100",
            "facility__description": "Suites",
            "number": 122,
            "group": "Location"
            },
            {
            "facility__group_code": 10,
            "facility": "10_132",
            "facility__description": "Twin rooms",
            "number": 1016,
            "group": "Location"
            },
            {
            "facility__group_code": 10,
            "facility": "10_20",
            "facility__description": "Year of construction",
            "number": 1972,
            "group": "Location"
            },
            {
            "facility__group_code": 10,
            "facility": "10_30",
            "facility__description": "Year of most recent renovation",
            "number": 2006,
            "group": "Location"
            },
            {
            "facility__group_code": 10,
            "facility": "10_50",
            "facility__description": "Number of floors (main building)",
            "number": 35,
            "group": "Location"
            },
            {
            "facility__group_code": 10,
            "facility": "10_70",
            "facility__description": "Total number of rooms",
            "number": 2019,
            "group": "Location"
            },
            {
            "facility__group_code": 10,
            "facility": "10_90",
            "facility__description": "Double rooms",
            "number": 894,
            "group": "Location"
            },
            {
            "facility__group_code": 20,
            "facility": "20_10",
            "facility__description": "hotel",
            "number": null,
            "group": "Hotel type"
            },
            {
            "facility__group_code": 30,
            "facility": "30_10",
            "facility__description": "American Express",
            "number": null,
            "group": "Methods of payment"
            },
            {
            "facility__group_code": 30,
            "facility": "30_30",
            "facility__description": "JCB",
            "number": null,
            "group": "Methods of payment"
            },
            {
            "facility__group_code": 30,
            "facility": "30_40",
            "facility__description": "Diners Club",
            "number": null,
            "group": "Methods of payment"
            },
            {
            "facility__group_code": 30,
            "facility": "30_50",
            "facility__description": "MasterCard",
            "number": null,
            "group": "Methods of payment"
            },
            {
            "facility__group_code": 30,
            "facility": "30_60",
            "facility__description": "Visa",
            "number": null,
            "group": "Methods of payment"
            },
            {
            "facility__group_code": 60,
            "facility": "60_10",
            "facility__description": "Bathroom",
            "number": null,
            "group": "Room facilities (Standard room)"
            },
            {
            "facility__group_code": 60,
            "facility": "60_100",
            "facility__description": "Internet access",
            "number": null,
            "group": "Room facilities (Standard room)"
            },
            {
            "facility__group_code": 60,
            "facility": "60_120",
            "facility__description": "Minibar",
            "number": null,
            "group": "Room facilities (Standard room)"
            },
            {
            "facility__group_code": 60,
            "facility": "60_143",
            "facility__description": "Tea and coffee making facilities",
            "number": null,
            "group": "Room facilities (Standard room)"
            },
            {
            "facility__group_code": 60,
            "facility": "60_147",
            "facility__description": "Ironing set",
            "number": null,
            "group": "Room facilities (Standard room)"
            },
            {
            "facility__group_code": 60,
            "facility": "60_160",
            "facility__description": "Carpeted floors",
            "number": null,
            "group": "Room facilities (Standard room)"
            },
            {
            "facility__group_code": 60,
            "facility": "60_180",
            "facility__description": "Individually adjustable air conditioning",
            "number": null,
            "group": "Room facilities (Standard room)"
            },
            {
            "facility__group_code": 60,
            "facility": "60_195",
            "facility__description": "Individually adjustable heating",
            "number": null,
            "group": "Room facilities (Standard room)"
            },
            {
            "facility__group_code": 60,
            "facility": "60_20",
            "facility__description": "Shower",
            "number": null,
            "group": "Room facilities (Standard room)"
            },
            {
            "facility__group_code": 60,
            "facility": "60_200",
            "facility__description": "Safe",
            "number": null,
            "group": "Room facilities (Standard room)"
            },
            {
            "facility__group_code": 60,
            "facility": "60_250",
            "facility__description": "Wheelchair-accessible",
            "number": null,
            "group": "Room facilities (Standard room)"
            },
            {
            "facility__group_code": 60,
            "facility": "60_260",
            "facility__description": "Disability-friendly bathroom",
            "number": null,
            "group": "Room facilities (Standard room)"
            },
            {
            "facility__group_code": 60,
            "facility": "60_261",
            "facility__description": "Wi-fi",
            "number": null,
            "group": "Room facilities (Standard room)"
            },
            {
            "facility__group_code": 60,
            "facility": "60_264",
            "facility__description": "Cot on demand",
            "number": null,
            "group": "Room facilities (Standard room)"
            },
            {
            "facility__group_code": 60,
            "facility": "60_275",
            "facility__description": "Extra beds on demand",
            "number": null,
            "group": "Room facilities (Standard room)"
            },
            {
            "facility__group_code": 60,
            "facility": "60_298",
            "facility__description": "Number of bedrooms",
            "number": 1,
            "group": "Room facilities (Standard room)"
            },
            {
            "facility__group_code": 60,
            "facility": "60_30",
            "facility__description": "Bathtub",
            "number": null,
            "group": "Room facilities (Standard room)"
            },
            {
            "facility__group_code": 60,
            "facility": "60_40",
            "facility__description": "Hairdryer",
            "number": null,
            "group": "Room facilities (Standard room)"
            },
            {
            "facility__group_code": 60,
            "facility": "60_50",
            "facility__description": "Direct dial telephone",
            "number": null,
            "group": "Room facilities (Standard room)"
            },
            {
            "facility__group_code": 60,
            "facility": "60_55",
            "facility__description": "TV",
            "number": null,
            "group": "Room facilities (Standard room)"
            },
            {
            "facility__group_code": 60,
            "facility": "60_80",
            "facility__description": "Radio",
            "number": null,
            "group": "Room facilities (Standard room)"
            },
            {
            "facility__group_code": 70,
            "facility": "70_10",
            "facility__description": "Air conditioning in public areas",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_11",
            "facility__description": "Fireplace",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_110",
            "facility__description": "Shop",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_135",
            "facility__description": "Terrace",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_260",
            "facility__description": "Check-in hour",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_270",
            "facility__description": "Room service",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_280",
            "facility__description": "Laundry service",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_285",
            "facility__description": "Launderette",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_295",
            "facility__description": "Wheelchair-accessible",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_30",
            "facility__description": "24-hour reception",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_320",
            "facility__description": "Car park",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_390",
            "facility__description": "Check-out hour",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_40",
            "facility__description": "Hotel safe",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_470",
            "facility__description": "Gym",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_485",
            "facility__description": "Babysitting service",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_490",
            "facility__description": "Car hire",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_50",
            "facility__description": "Currency exchange facilities",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_500",
            "facility__description": "Secure parking",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_505",
            "facility__description": "Multilingual staff",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_515",
            "facility__description": "Newspapers",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_520",
            "facility__description": "24-hour security",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_525",
            "facility__description": "Bellboy service",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_550",
            "facility__description": "Wi-fi",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_559",
            "facility__description": "Luggage room",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_560",
            "facility__description": "Valet parking",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_564",
            "facility__description": "Late Check-out",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_568",
            "facility__description": "Clothes dryer",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_585",
            "facility__description": "Concierge",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_60",
            "facility__description": "Cloakroom",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_70",
            "facility__description": "Lift access",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 70,
            "facility": "70_90",
            "facility__description": "Newspaper stand",
            "number": null,
            "group": "Facilities"
            },
            {
            "facility__group_code": 71,
            "facility": "71_130",
            "facility__description": "Bar",
            "number": null,
            "group": "Catering"
            },
            {
            "facility__group_code": 71,
            "facility": "71_200",
            "facility__description": "Restaurant",
            "number": 4,
            "group": "Catering"
            },
            {
            "facility__group_code": 71,
            "facility": "71_225",
            "facility__description": "Smoking area",
            "number": null,
            "group": "Catering"
            },
            {
            "facility__group_code": 71,
            "facility": "71_575",
            "facility__description": "Air conditioning in Restaurant",
            "number": null,
            "group": "Catering"
            },
            {
            "facility__group_code": 72,
            "facility": "72_170",
            "facility__description": "Conference room",
            "number": null,
            "group": "Business"
            },
            {
            "facility__group_code": 72,
            "facility": "72_575",
            "facility__description": "Meeting room",
            "number": null,
            "group": "Business"
            },
            {
            "facility__group_code": 72,
            "facility": "72_605",
            "facility__description": "Business centre",
            "number": null,
            "group": "Business"
            },
            {
            "facility__group_code": 74,
            "facility": "74_120",
            "facility__description": "Hairdressing salon",
            "number": null,
            "group": "Health"
            },
            {
            "facility__group_code": 74,
            "facility": "74_410",
            "facility__description": "Hot tub",
            "number": null,
            "group": "Health"
            },
            {
            "facility__group_code": 75,
            "facility": "75_850",
            "facility__description": "Green Key Global",
            "number": null,
            "group": "Green Programmes - Worldwide"
            },
            {
            "facility__group_code": 85,
            "facility": "85_562",
            "facility__description": "Non-smoking establishment",
            "number": null,
            "group": "Things to keep in mind"
            },
            {
            "facility__group_code": 90,
            "facility": "90_295",
            "facility__description": "Fitness",
            "number": null,
            "group": "Sports"
            },
            {
            "facility__group_code": 90,
            "facility": "90_390",
            "facility__description": "Golf",
            "number": null,
            "group": "Sports"
            },
            {
            "facility__group_code": 90,
            "facility": "90_520",
            "facility__description": "Golf practice facility",
            "number": null,
            "group": "Sports"
            },
            {
            "facility__group_code": 91,
            "facility": "91_8",
            "facility__description": "Hyatt - GBAC STAR Global Care & Cleanliness Commitment",
            "number": null,
            "group": "Healthy & Safety (COVID)"
            }
        ],
        "top_facilities": [
            {
            "id": 1,
            "facility_id": "70_550",
            "icon": "outline_wifi_black_24dp.png",
            "name": "Wi-fi",
            "other_names": "Free WiFi",
            "dir": "wifi"
            },
            {
            "id": 2,
            "facility_id": "70_320",
            "icon": "outline_local_parking_black_24dp.png",
            "name": "Car park",
            "other_names": "Parking",
            "dir": "parking"
            },
            {
            "id": 3,
            "facility_id": "70_30",
            "icon": "outline_local_convenience_store_black_24dp.png",
            "name": "24-hour reception",
            "other_names": "24-hour front desk",
            "dir": "24-hour reception"
            },
            {
            "id": 4,
            "facility_id": "60_250",
            "icon": "outline_accessible_black_24dp.png",
            "name": "Wheelchair-accessible",
            "other_names": "Facilities for disabled guests",
            "dir": "disabled_facilities"
            },
            {
            "id": 5,
            "facility_id": "85_562",
            "icon": "outline_smoke_free_black_24dp.png",
            "name": "Non-smoking establishment",
            "other_names": "Non-smoking rooms",
            "dir": "non-smoking_rooms"
            },
            {
            "id": 9,
            "facility_id": "90_295",
            "icon": "outline_fitness_center_black_24dp.png",
            "name": "Fitness",
            "other_names": "Fitness center",
            "dir": "fitness_center"
            },
            {
            "id": 10,
            "facility_id": "70_470",
            "icon": "outline_fitness_center_black_24dp.png",
            "name": "Gym",
            "other_names": "Fitness center",
            "dir": "fitness_center"
            },
            {
            "id": 11,
            "facility_id": "70_270",
            "icon": "outline_room_service_black_24dp.png",
            "name": "Room service",
            "other_names": "Room service",
            "dir": "room_service"
            },
            {
            "id": 12,
            "facility_id": "71_200",
            "icon": "outline_restaurant_menu_black_24dp.png",
            "name": "Restaurant",
            "other_names": "Restaurant",
            "dir": "restaurant"
            },
            {
            "id": 15,
            "facility_id": "71_130",
            "icon": "outline_local_bar_black_24dp.png",
            "name": "Bar",
            "other_names": "Bar",
            "dir": "bar"
            },
            {
            "id": 16,
            "facility_id": "60_143",
            "icon": "outline_coffee_maker_black_24dp.png",
            "name": "Tea and coffee making facilities",
            "other_names": "Tea/Coffee Maker in All Rooms",
            "dir": "tea_coffee_making_facilities"
            },
            {
            "id": 17,
            "facility_id": "70_10",
            "icon": "outline_ac_unit_black_24dp.png",
            "name": "Air conditioning in public areas",
            "other_names": "Air conditioning",
            "dir": "air_conditioning"
            },
            {
            "id": 19,
            "facility_id": "74_410",
            "icon": "outline_hot_tub_black_24dp.png",
            "name": "Hot tub",
            "other_names": "Hot tub",
            "dir": "hot_tub"
            },
            {
            "id": 21,
            "facility_id": "70_280",
            "icon": "outline_local_laundry_service_black_24dp.png",
            "name": "Laundry service",
            "other_names": "Laundry service",
            "dir": "laundry_service"
            }
        ],
        "rooms": [
            {
            "code": "900103035",
            "name": "King Room",
            "description": "This room includes a coffee machine and a private bathroom with a shower.",
            "rates": [
                {
                "rateClass": "NRF",
                "rateType": "RECHECK",
                "allotment": 516,
                "paymentType": "AT_WEB",
                "packaging": false,
                "boardCode": "RO",
                "cancellationPolicies": [
                    {
                    "from": "2020-08-29T17:00:00-05:00",
                    "penaltyAmount": "338.07",
                    "displayCurrency": {
                        "USD": {
                        "penaltyAmount": "338.07"
                        },
                        "CAD": {
                        "penaltyAmount": "462.15"
                        },
                        "EUR": {
                        "penaltyAmount": "311.63"
                        },
                        "GBP": {
                        "penaltyAmount": "265.48"
                        },
                        "AUD": {
                        "penaltyAmount": "510.47"
                        }
                    }
                    }
                ],
                "rooms": 1,
                "adults": 2,
                "children": 0,
                "cancellationPolicy": "\u003Cb\u003ECancellation Policy\u003C/b\u003E\u003Cp\u003EIf you do not check in to the hotel on the first day of your reservation and do not alert the hotel in advance, the hotel reserves the right to cancel your reservation and you may be charged for the full amount.\u003C/p\u003E",
                "rateComments": "\u003Cb\u003ECancellation Policy\u003C/b\u003E\u003Cp\u003EIf you do not check in to the hotel on the first day of your reservation and do not alert the hotel in advance, the hotel reserves the right to cancel your reservation and you may be charged for the full amount.\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003ERefund Policy\u003C/b\u003E\u003Cp\u003EAny cancellation received within 2 days prior to arrival date will incur the first night charge. Failure to arrive at your hotel or property will be treated as a No-Show and no refund will be given (Property policy).\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EPhoto Policy\u003C/b\u003E\u003Cp\u003EThe reservation holder must present a valid photo ID and credit card at check-in. The credit card is required for \u003Cb\u003Ethe mandatory fee listed above as well as\u003C/b\u003E any additional hotel incidental charges such as parking, phone calls or minibar charges which are not included in the room rate.\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EPromo has been applied\u003C/b\u003E\u003Cp\u003E\u003Cb\u003ENegotiated Special Details:\u003C/b\u003E\u003Cli\u003E\u003Cem\u003EOn Sale Now -\u003E Save 10% on this stay\u003C/em\u003E&nbsp;&#151;&nbsp;Book Now and Save\u003C/li\u003E\u003Cli\u003EOffer Details:&nbsp;Negotiated Specials may be limited to certain dates and subject to availability.\u003C/li\u003E\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003ERate Description\u003C/b\u003E\u003Cp\u003ESpecial Rate\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EHotel Occupancy Policy\u003C/b\u003E\u003Cp\u003EAll rooms booked for triple occupancy (i.e. 3 adults). Accommodations for more than this are not guaranteed.\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003ERoom Charge Disclosure\u003C/b\u003E\u003Cp\u003EYour credit card is charged the total cost at time of purchase. Prices and room availability are not guaranteed until full payment is received.\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EHotel Pet Policy\u003C/b\u003E\u003Cp\u003EPets are not allowed.\n\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EImportant Information\u003C/b\u003E\u003Cp\u003EGuests are required to show a photo ID and credit card upon check-in. Please note that all Special Requests are subject to availability and additional charges may apply. Bookings on and beyond January 01, 2024 - A daily destination fee of $25.00 pretax (subject to change) is applied to each room of your stay in order to provide the following services and amenities, which enhance the guest experience. Please find below the services and experience: · Daily $25 Dining Credit for Lunch or Dinner in any of our outlets · Daily Premium Guest room Internet · Discounted Daily Parking · 10% Discount on Luxury Car Service through our preferred transportation provider · 20% Discount on apparel in Market Chicago · Discounted Access to Lake Shore Fitness · 15% discount on shoe shines provided by Spa Di Lafronza\u003C/p\u003E",
                "isRefundable": false,
                "isPartialRefundable": false,
                "cancellationPenaltyRate": "1.0",
                "ppnPropertyId": 700024973,
                "rateId": "66541893-fb44-0401-517d-5300af160108",
                "baseRate": "293.98",
                "tax": "44.10",
                "otherFees": "29.35",
                "chargeAmount": "338.08",
                "strikeThroughPrice": "524.00",
                "displayCurrency": {
                    "USD": {
                    "baseRate": "293.98",
                    "tax": "44.10",
                    "chargeAmount": "338.07",
                    "otherFees": "29.35",
                    "strikeThroughPrice": "524.00"
                    },
                    "CAD": {
                    "baseRate": "401.87",
                    "tax": "60.28",
                    "chargeAmount": "462.15",
                    "otherFees": "40.12",
                    "strikeThroughPrice": "716.32"
                    },
                    "EUR": {
                    "baseRate": "270.98",
                    "tax": "40.65",
                    "chargeAmount": "311.63",
                    "otherFees": "27.05",
                    "strikeThroughPrice": "483.02"
                    },
                    "GBP": {
                    "baseRate": "230.86",
                    "tax": "34.63",
                    "chargeAmount": "265.48",
                    "otherFees": "23.05",
                    "strikeThroughPrice": "411.49"
                    },
                    "AUD": {
                    "baseRate": "443.89",
                    "tax": "66.58",
                    "chargeAmount": "510.47",
                    "otherFees": "44.32",
                    "strikeThroughPrice": "791.21"
                    }
                }
                }
            ],
            "beds": null,
            "roomImages": [
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/488804542.jpg?k=927df5d062c43388e2570d65be3dc715daf179f5d4e0a3cb4d3f8ba09d218d07&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/488804542.jpg?k=927df5d062c43388e2570d65be3dc715daf179f5d4e0a3cb4d3f8ba09d218d07&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/488804542.jpg?k=927df5d062c43388e2570d65be3dc715daf179f5d4e0a3cb4d3f8ba09d218d07&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/488804487.jpg?k=7a6cfe4428d0b82dabf3a479c2e6241ebd3f1f73b029717273824a84f4d5561f&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/488804487.jpg?k=7a6cfe4428d0b82dabf3a479c2e6241ebd3f1f73b029717273824a84f4d5561f&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/488804487.jpg?k=7a6cfe4428d0b82dabf3a479c2e6241ebd3f1f73b029717273824a84f4d5561f&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/488804648.jpg?k=d0a3dd56f5bc0a089ed9792bdae248b1e0f8c72fc1989f4686f21893492e75e8&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/488804648.jpg?k=d0a3dd56f5bc0a089ed9792bdae248b1e0f8c72fc1989f4686f21893492e75e8&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/488804648.jpg?k=d0a3dd56f5bc0a089ed9792bdae248b1e0f8c72fc1989f4686f21893492e75e8&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/516202048.jpg?k=a7c95746980100b2cadb3720af2690db66f2aab68fdb9ca5661688d313a90e3d&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/516202048.jpg?k=a7c95746980100b2cadb3720af2690db66f2aab68fdb9ca5661688d313a90e3d&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/516202048.jpg?k=a7c95746980100b2cadb3720af2690db66f2aab68fdb9ca5661688d313a90e3d&o="
                }
            ],
            "facilities": [],
            "top_facilities": []
            },
            {
            "code": "900103044",
            "name": "Queen Room with Two Queen Beds and Accessible Tub - Disability Access",
            "description": "Featuring a handicap accessible bath, this room also offers a private bathroom with wide doors, grab bars and a raised toilet seat.",
            "rates": [
                {
                "rateClass": "NRF",
                "rateType": "RECHECK",
                "allotment": 2,
                "paymentType": "AT_WEB",
                "packaging": false,
                "boardCode": "RO",
                "cancellationPolicies": [
                    {
                    "from": "2020-08-29T17:00:00-05:00",
                    "penaltyAmount": "339.30",
                    "displayCurrency": {
                        "USD": {
                        "penaltyAmount": "339.30"
                        },
                        "CAD": {
                        "penaltyAmount": "463.83"
                        },
                        "EUR": {
                        "penaltyAmount": "312.76"
                        },
                        "GBP": {
                        "penaltyAmount": "266.45"
                        },
                        "AUD": {
                        "penaltyAmount": "512.32"
                        }
                    }
                    }
                ],
                "rooms": 1,
                "adults": 2,
                "children": 0,
                "cancellationPolicy": "\u003Cb\u003ECancellation Policy\u003C/b\u003E\u003Cp\u003EIf you do not check in to the hotel on the first day of your reservation and do not alert the hotel in advance, the hotel reserves the right to cancel your reservation and you may be charged for the full amount.\u003C/p\u003E",
                "rateComments": "\u003Cb\u003ECancellation Policy\u003C/b\u003E\u003Cp\u003EIf you do not check in to the hotel on the first day of your reservation and do not alert the hotel in advance, the hotel reserves the right to cancel your reservation and you may be charged for the full amount.\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003ERefund Policy\u003C/b\u003E\u003Cp\u003EAny cancellation received within 2 days prior to arrival date will incur the first night charge. Failure to arrive at your hotel or property will be treated as a No-Show and no refund will be given (Property policy).\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EPhoto Policy\u003C/b\u003E\u003Cp\u003EThe reservation holder must present a valid photo ID and credit card at check-in. The credit card is required for \u003Cb\u003Ethe mandatory fee listed above as well as\u003C/b\u003E any additional hotel incidental charges such as parking, phone calls or minibar charges which are not included in the room rate.\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EPromo has been applied\u003C/b\u003E\u003Cp\u003E\u003Cb\u003ENegotiated Special Details:\u003C/b\u003E\u003Cli\u003E\u003Cem\u003EOn Sale Now -\u003E Save 10% on this stay\u003C/em\u003E&nbsp;&#151;&nbsp;Book Now and Save\u003C/li\u003E\u003Cli\u003EOffer Details:&nbsp;Negotiated Specials may be limited to certain dates and subject to availability.\u003C/li\u003E\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003ERate Description\u003C/b\u003E\u003Cp\u003ESpecial Rate\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EHotel Occupancy Policy\u003C/b\u003E\u003Cp\u003EAll rooms booked for triple occupancy (i.e. 3 adults). Accommodations for more than this are not guaranteed.\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003ERoom Charge Disclosure\u003C/b\u003E\u003Cp\u003EYour credit card is charged the total cost at time of purchase. Prices and room availability are not guaranteed until full payment is received.\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EHotel Pet Policy\u003C/b\u003E\u003Cp\u003EPets are not allowed.\n\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EImportant Information\u003C/b\u003E\u003Cp\u003EGuests are required to show a photo ID and credit card upon check-in. Please note that all Special Requests are subject to availability and additional charges may apply. Bookings on and beyond January 01, 2024 - A daily destination fee of $25.00 pretax (subject to change) is applied to each room of your stay in order to provide the following services and amenities, which enhance the guest experience. Please find below the services and experience: · Daily $25 Dining Credit for Lunch or Dinner in any of our outlets · Daily Premium Guest room Internet · Discounted Daily Parking · 10% Discount on Luxury Car Service through our preferred transportation provider · 20% Discount on apparel in Market Chicago · Discounted Access to Lake Shore Fitness · 15% discount on shoe shines provided by Spa Di Lafronza\u003C/p\u003E",
                "isRefundable": false,
                "isPartialRefundable": false,
                "cancellationPenaltyRate": "1.0",
                "ppnPropertyId": 700024973,
                "rateId": "66541893-fb4b-0401-8e64-279105413f0a",
                "baseRate": "295.04",
                "tax": "44.26",
                "otherFees": "29.35",
                "chargeAmount": "339.30",
                "strikeThroughPrice": "524.00",
                "displayCurrency": {
                    "USD": {
                    "baseRate": "295.04",
                    "tax": "44.26",
                    "chargeAmount": "339.30",
                    "otherFees": "29.35",
                    "strikeThroughPrice": "524.00"
                    },
                    "CAD": {
                    "baseRate": "403.33",
                    "tax": "60.50",
                    "chargeAmount": "463.83",
                    "otherFees": "40.12",
                    "strikeThroughPrice": "716.32"
                    },
                    "EUR": {
                    "baseRate": "271.97",
                    "tax": "40.80",
                    "chargeAmount": "312.76",
                    "otherFees": "27.05",
                    "strikeThroughPrice": "483.02"
                    },
                    "GBP": {
                    "baseRate": "231.69",
                    "tax": "34.75",
                    "chargeAmount": "266.45",
                    "otherFees": "23.05",
                    "strikeThroughPrice": "411.49"
                    },
                    "AUD": {
                    "baseRate": "445.50",
                    "tax": "66.82",
                    "chargeAmount": "512.32",
                    "otherFees": "44.32",
                    "strikeThroughPrice": "791.21"
                    }
                }
                }
            ],
            "beds": null,
            "roomImages": [
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/488805200.jpg?k=d5e281bf836d6f8d9251741ad4a037fcfbf1d52de31404fec600ef980e74e001&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/488805200.jpg?k=d5e281bf836d6f8d9251741ad4a037fcfbf1d52de31404fec600ef980e74e001&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/488805200.jpg?k=d5e281bf836d6f8d9251741ad4a037fcfbf1d52de31404fec600ef980e74e001&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/488805167.jpg?k=ea2fedaa722a20f83a758f9aa83b60c3a7ac322555a65fce17965259e5e1f51e&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/488805167.jpg?k=ea2fedaa722a20f83a758f9aa83b60c3a7ac322555a65fce17965259e5e1f51e&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/488805167.jpg?k=ea2fedaa722a20f83a758f9aa83b60c3a7ac322555a65fce17965259e5e1f51e&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/516312401.jpg?k=6583ddc924a7e0666d63f8bc3339834bf977b00387bec3259427bbad66373386&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/516312401.jpg?k=6583ddc924a7e0666d63f8bc3339834bf977b00387bec3259427bbad66373386&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/516312401.jpg?k=6583ddc924a7e0666d63f8bc3339834bf977b00387bec3259427bbad66373386&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/488805796.jpg?k=8bcab6233993b75cc06bc3f512e923007e78b569715ac99c4637c1679ebd1108&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/488805796.jpg?k=8bcab6233993b75cc06bc3f512e923007e78b569715ac99c4637c1679ebd1108&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/488805796.jpg?k=8bcab6233993b75cc06bc3f512e923007e78b569715ac99c4637c1679ebd1108&o="
                }
            ],
            "facilities": [],
            "top_facilities": []
            },
            {
            "code": "900103038",
            "name": "King Room with Accessible Shower - Disability Access",
            "description": "Featuring a handicap accessible shower, this room also offers a private bathroom with wide doors, grab bars and a raised toilet seat.",
            "rates": [
                {
                "rateClass": "NRF",
                "rateType": "RECHECK",
                "allotment": 5,
                "paymentType": "AT_WEB",
                "packaging": false,
                "boardCode": "RO",
                "cancellationPolicies": [
                    {
                    "from": "2020-08-29T17:00:00-05:00",
                    "penaltyAmount": "339.30",
                    "displayCurrency": {
                        "USD": {
                        "penaltyAmount": "339.30"
                        },
                        "CAD": {
                        "penaltyAmount": "463.83"
                        },
                        "EUR": {
                        "penaltyAmount": "312.76"
                        },
                        "GBP": {
                        "penaltyAmount": "266.45"
                        },
                        "AUD": {
                        "penaltyAmount": "512.32"
                        }
                    }
                    }
                ],
                "rooms": 1,
                "adults": 2,
                "children": 0,
                "cancellationPolicy": "\u003Cb\u003ECancellation Policy\u003C/b\u003E\u003Cp\u003EIf you do not check in to the hotel on the first day of your reservation and do not alert the hotel in advance, the hotel reserves the right to cancel your reservation and you may be charged for the full amount.\u003C/p\u003E",
                "rateComments": "\u003Cb\u003ECancellation Policy\u003C/b\u003E\u003Cp\u003EIf you do not check in to the hotel on the first day of your reservation and do not alert the hotel in advance, the hotel reserves the right to cancel your reservation and you may be charged for the full amount.\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003ERefund Policy\u003C/b\u003E\u003Cp\u003EAny cancellation received within 2 days prior to arrival date will incur the first night charge. Failure to arrive at your hotel or property will be treated as a No-Show and no refund will be given (Property policy).\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EPhoto Policy\u003C/b\u003E\u003Cp\u003EThe reservation holder must present a valid photo ID and credit card at check-in. The credit card is required for \u003Cb\u003Ethe mandatory fee listed above as well as\u003C/b\u003E any additional hotel incidental charges such as parking, phone calls or minibar charges which are not included in the room rate.\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EPromo has been applied\u003C/b\u003E\u003Cp\u003E\u003Cb\u003ENegotiated Special Details:\u003C/b\u003E\u003Cli\u003E\u003Cem\u003EOn Sale Now -\u003E Save 10% on this stay\u003C/em\u003E&nbsp;&#151;&nbsp;Book Now and Save\u003C/li\u003E\u003Cli\u003EOffer Details:&nbsp;Negotiated Specials may be limited to certain dates and subject to availability.\u003C/li\u003E\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003ERate Description\u003C/b\u003E\u003Cp\u003ESpecial Rate\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EHotel Occupancy Policy\u003C/b\u003E\u003Cp\u003EAll rooms booked for triple occupancy (i.e. 3 adults). Accommodations for more than this are not guaranteed.\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003ERoom Charge Disclosure\u003C/b\u003E\u003Cp\u003EYour credit card is charged the total cost at time of purchase. Prices and room availability are not guaranteed until full payment is received.\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EHotel Pet Policy\u003C/b\u003E\u003Cp\u003EPets are not allowed.\n\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EImportant Information\u003C/b\u003E\u003Cp\u003EGuests are required to show a photo ID and credit card upon check-in. Please note that all Special Requests are subject to availability and additional charges may apply. Bookings on and beyond January 01, 2024 - A daily destination fee of $25.00 pretax (subject to change) is applied to each room of your stay in order to provide the following services and amenities, which enhance the guest experience. Please find below the services and experience: · Daily $25 Dining Credit for Lunch or Dinner in any of our outlets · Daily Premium Guest room Internet · Discounted Daily Parking · 10% Discount on Luxury Car Service through our preferred transportation provider · 20% Discount on apparel in Market Chicago · Discounted Access to Lake Shore Fitness · 15% discount on shoe shines provided by Spa Di Lafronza\u003C/p\u003E",
                "isRefundable": false,
                "isPartialRefundable": false,
                "cancellationPenaltyRate": "1.0",
                "ppnPropertyId": 700024973,
                "rateId": "66541893-fb4e-0401-bc9a-4d4755002890",
                "baseRate": "295.04",
                "tax": "44.26",
                "otherFees": "29.35",
                "chargeAmount": "339.30",
                "strikeThroughPrice": "524.00",
                "displayCurrency": {
                    "USD": {
                    "baseRate": "295.04",
                    "tax": "44.26",
                    "chargeAmount": "339.30",
                    "otherFees": "29.35",
                    "strikeThroughPrice": "524.00"
                    },
                    "CAD": {
                    "baseRate": "403.33",
                    "tax": "60.50",
                    "chargeAmount": "463.83",
                    "otherFees": "40.12",
                    "strikeThroughPrice": "716.32"
                    },
                    "EUR": {
                    "baseRate": "271.97",
                    "tax": "40.80",
                    "chargeAmount": "312.76",
                    "otherFees": "27.05",
                    "strikeThroughPrice": "483.02"
                    },
                    "GBP": {
                    "baseRate": "231.69",
                    "tax": "34.75",
                    "chargeAmount": "266.45",
                    "otherFees": "23.05",
                    "strikeThroughPrice": "411.49"
                    },
                    "AUD": {
                    "baseRate": "445.50",
                    "tax": "66.82",
                    "chargeAmount": "512.32",
                    "otherFees": "44.32",
                    "strikeThroughPrice": "791.21"
                    }
                }
                }
            ],
            "beds": null,
            "roomImages": [
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/488804542.jpg?k=927df5d062c43388e2570d65be3dc715daf179f5d4e0a3cb4d3f8ba09d218d07&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/488804542.jpg?k=927df5d062c43388e2570d65be3dc715daf179f5d4e0a3cb4d3f8ba09d218d07&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/488804542.jpg?k=927df5d062c43388e2570d65be3dc715daf179f5d4e0a3cb4d3f8ba09d218d07&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/488804487.jpg?k=7a6cfe4428d0b82dabf3a479c2e6241ebd3f1f73b029717273824a84f4d5561f&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/488804487.jpg?k=7a6cfe4428d0b82dabf3a479c2e6241ebd3f1f73b029717273824a84f4d5561f&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/488804487.jpg?k=7a6cfe4428d0b82dabf3a479c2e6241ebd3f1f73b029717273824a84f4d5561f&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/488804648.jpg?k=d0a3dd56f5bc0a089ed9792bdae248b1e0f8c72fc1989f4686f21893492e75e8&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/488804648.jpg?k=d0a3dd56f5bc0a089ed9792bdae248b1e0f8c72fc1989f4686f21893492e75e8&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/488804648.jpg?k=d0a3dd56f5bc0a089ed9792bdae248b1e0f8c72fc1989f4686f21893492e75e8&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/516312394.jpg?k=7cb8880faa75d3377ab3ffc5fe5e4ddf22159b37138fe644cb07bfcfbd37fffe&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/516312394.jpg?k=7cb8880faa75d3377ab3ffc5fe5e4ddf22159b37138fe644cb07bfcfbd37fffe&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/516312394.jpg?k=7cb8880faa75d3377ab3ffc5fe5e4ddf22159b37138fe644cb07bfcfbd37fffe&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/488805689.jpg?k=f965301d98996db5cfc2851b530b1fcd8cadf0084571443c5a92647688e8b0f8&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/488805689.jpg?k=f965301d98996db5cfc2851b530b1fcd8cadf0084571443c5a92647688e8b0f8&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/488805689.jpg?k=f965301d98996db5cfc2851b530b1fcd8cadf0084571443c5a92647688e8b0f8&o="
                }
            ],
            "facilities": [],
            "top_facilities": []
            },
            {
            "code": "900103046",
            "name": "Queen Room with Two Queen Beds",
            "description": "This room includes a coffee machine and a private bathroom with a shower.",
            "rates": [
                {
                "rateClass": "NRF",
                "rateType": "RECHECK",
                "allotment": 42,
                "paymentType": "AT_WEB",
                "packaging": false,
                "boardCode": "RO",
                "cancellationPolicies": [
                    {
                    "from": "2020-08-29T17:00:00-05:00",
                    "penaltyAmount": "339.30",
                    "displayCurrency": {
                        "USD": {
                        "penaltyAmount": "339.30"
                        },
                        "CAD": {
                        "penaltyAmount": "463.83"
                        },
                        "EUR": {
                        "penaltyAmount": "312.76"
                        },
                        "GBP": {
                        "penaltyAmount": "266.45"
                        },
                        "AUD": {
                        "penaltyAmount": "512.32"
                        }
                    }
                    }
                ],
                "rooms": 1,
                "adults": 2,
                "children": 0,
                "cancellationPolicy": "\u003Cb\u003ECancellation Policy\u003C/b\u003E\u003Cp\u003EIf you do not check in to the hotel on the first day of your reservation and do not alert the hotel in advance, the hotel reserves the right to cancel your reservation and you may be charged for the full amount.\u003C/p\u003E",
                "rateComments": "\u003Cb\u003ECancellation Policy\u003C/b\u003E\u003Cp\u003EIf you do not check in to the hotel on the first day of your reservation and do not alert the hotel in advance, the hotel reserves the right to cancel your reservation and you may be charged for the full amount.\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003ERefund Policy\u003C/b\u003E\u003Cp\u003EAny cancellation received within 2 days prior to arrival date will incur the first night charge. Failure to arrive at your hotel or property will be treated as a No-Show and no refund will be given (Property policy).\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EPhoto Policy\u003C/b\u003E\u003Cp\u003EThe reservation holder must present a valid photo ID and credit card at check-in. The credit card is required for \u003Cb\u003Ethe mandatory fee listed above as well as\u003C/b\u003E any additional hotel incidental charges such as parking, phone calls or minibar charges which are not included in the room rate.\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EPromo has been applied\u003C/b\u003E\u003Cp\u003E\u003Cb\u003ENegotiated Special Details:\u003C/b\u003E\u003Cli\u003E\u003Cem\u003EOn Sale Now -\u003E Save 10% on this stay\u003C/em\u003E&nbsp;&#151;&nbsp;Book Now and Save\u003C/li\u003E\u003Cli\u003EOffer Details:&nbsp;Negotiated Specials may be limited to certain dates and subject to availability.\u003C/li\u003E\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003ERate Description\u003C/b\u003E\u003Cp\u003ESpecial Rate\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EHotel Occupancy Policy\u003C/b\u003E\u003Cp\u003EAll rooms booked for triple occupancy (i.e. 3 adults). Accommodations for more than this are not guaranteed.\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003ERoom Charge Disclosure\u003C/b\u003E\u003Cp\u003EYour credit card is charged the total cost at time of purchase. Prices and room availability are not guaranteed until full payment is received.\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EHotel Pet Policy\u003C/b\u003E\u003Cp\u003EPets are not allowed.\n\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EImportant Information\u003C/b\u003E\u003Cp\u003EGuests are required to show a photo ID and credit card upon check-in. Please note that all Special Requests are subject to availability and additional charges may apply. Bookings on and beyond January 01, 2024 - A daily destination fee of $25.00 pretax (subject to change) is applied to each room of your stay in order to provide the following services and amenities, which enhance the guest experience. Please find below the services and experience: · Daily $25 Dining Credit for Lunch or Dinner in any of our outlets · Daily Premium Guest room Internet · Discounted Daily Parking · 10% Discount on Luxury Car Service through our preferred transportation provider · 20% Discount on apparel in Market Chicago · Discounted Access to Lake Shore Fitness · 15% discount on shoe shines provided by Spa Di Lafronza\u003C/p\u003E",
                "isRefundable": false,
                "isPartialRefundable": false,
                "cancellationPenaltyRate": "1.0",
                "ppnPropertyId": 700024973,
                "rateId": "66541893-fb51-0401-5d54-8865ab68be8b",
                "baseRate": "295.04",
                "tax": "44.26",
                "otherFees": "29.35",
                "chargeAmount": "339.30",
                "strikeThroughPrice": "524.00",
                "displayCurrency": {
                    "USD": {
                    "baseRate": "295.04",
                    "tax": "44.26",
                    "chargeAmount": "339.30",
                    "otherFees": "29.35",
                    "strikeThroughPrice": "524.00"
                    },
                    "CAD": {
                    "baseRate": "403.33",
                    "tax": "60.50",
                    "chargeAmount": "463.83",
                    "otherFees": "40.12",
                    "strikeThroughPrice": "716.32"
                    },
                    "EUR": {
                    "baseRate": "271.97",
                    "tax": "40.80",
                    "chargeAmount": "312.76",
                    "otherFees": "27.05",
                    "strikeThroughPrice": "483.02"
                    },
                    "GBP": {
                    "baseRate": "231.69",
                    "tax": "34.75",
                    "chargeAmount": "266.45",
                    "otherFees": "23.05",
                    "strikeThroughPrice": "411.49"
                    },
                    "AUD": {
                    "baseRate": "445.50",
                    "tax": "66.82",
                    "chargeAmount": "512.32",
                    "otherFees": "44.32",
                    "strikeThroughPrice": "791.21"
                    }
                }
                }
            ],
            "beds": null,
            "roomImages": [
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/488805167.jpg?k=ea2fedaa722a20f83a758f9aa83b60c3a7ac322555a65fce17965259e5e1f51e&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/488805167.jpg?k=ea2fedaa722a20f83a758f9aa83b60c3a7ac322555a65fce17965259e5e1f51e&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/488805167.jpg?k=ea2fedaa722a20f83a758f9aa83b60c3a7ac322555a65fce17965259e5e1f51e&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/488805200.jpg?k=d5e281bf836d6f8d9251741ad4a037fcfbf1d52de31404fec600ef980e74e001&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/488805200.jpg?k=d5e281bf836d6f8d9251741ad4a037fcfbf1d52de31404fec600ef980e74e001&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/488805200.jpg?k=d5e281bf836d6f8d9251741ad4a037fcfbf1d52de31404fec600ef980e74e001&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/516202048.jpg?k=a7c95746980100b2cadb3720af2690db66f2aab68fdb9ca5661688d313a90e3d&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/516202048.jpg?k=a7c95746980100b2cadb3720af2690db66f2aab68fdb9ca5661688d313a90e3d&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/516202048.jpg?k=a7c95746980100b2cadb3720af2690db66f2aab68fdb9ca5661688d313a90e3d&o="
                }
            ],
            "facilities": [],
            "top_facilities": []
            },
            {
            "code": "900103045",
            "name": "King Room with City View",
            "description": "This room offers scenic views of either downtown Chicago, the Chicago River or Lake Michigan.",
            "rates": [
                {
                "rateClass": "NRF",
                "rateType": "RECHECK",
                "allotment": 70,
                "paymentType": "AT_WEB",
                "packaging": false,
                "boardCode": "RO",
                "cancellationPolicies": [
                    {
                    "from": "2020-08-29T17:00:00-05:00",
                    "penaltyAmount": "365.40",
                    "displayCurrency": {
                        "USD": {
                        "penaltyAmount": "365.40"
                        },
                        "CAD": {
                        "penaltyAmount": "499.51"
                        },
                        "EUR": {
                        "penaltyAmount": "336.82"
                        },
                        "GBP": {
                        "penaltyAmount": "286.94"
                        },
                        "AUD": {
                        "penaltyAmount": "551.73"
                        }
                    }
                    }
                ],
                "rooms": 1,
                "adults": 2,
                "children": 0,
                "cancellationPolicy": "\u003Cb\u003ECancellation Policy\u003C/b\u003E\u003Cp\u003EIf you do not check in to the hotel on the first day of your reservation and do not alert the hotel in advance, the hotel reserves the right to cancel your reservation and you may be charged for the full amount.\u003C/p\u003E",
                "rateComments": "\u003Cb\u003ECancellation Policy\u003C/b\u003E\u003Cp\u003EIf you do not check in to the hotel on the first day of your reservation and do not alert the hotel in advance, the hotel reserves the right to cancel your reservation and you may be charged for the full amount.\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003ERefund Policy\u003C/b\u003E\u003Cp\u003EAny cancellation received within 2 days prior to arrival date will incur the first night charge. Failure to arrive at your hotel or property will be treated as a No-Show and no refund will be given (Property policy).\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EPhoto Policy\u003C/b\u003E\u003Cp\u003EThe reservation holder must present a valid photo ID and credit card at check-in. The credit card is required for \u003Cb\u003Ethe mandatory fee listed above as well as\u003C/b\u003E any additional hotel incidental charges such as parking, phone calls or minibar charges which are not included in the room rate.\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EPromo has been applied\u003C/b\u003E\u003Cp\u003E\u003Cb\u003ENegotiated Special Details:\u003C/b\u003E\u003Cli\u003E\u003Cem\u003EOn Sale Now -\u003E Save 10% on this stay\u003C/em\u003E&nbsp;&#151;&nbsp;Book Now and Save\u003C/li\u003E\u003Cli\u003EOffer Details:&nbsp;Negotiated Specials may be limited to certain dates and subject to availability.\u003C/li\u003E\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003ERate Description\u003C/b\u003E\u003Cp\u003ESpecial Rate\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EHotel Occupancy Policy\u003C/b\u003E\u003Cp\u003EAll rooms booked for triple occupancy (i.e. 3 adults). Accommodations for more than this are not guaranteed.\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003ERoom Charge Disclosure\u003C/b\u003E\u003Cp\u003EYour credit card is charged the total cost at time of purchase. Prices and room availability are not guaranteed until full payment is received.\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EHotel Pet Policy\u003C/b\u003E\u003Cp\u003EPets are not allowed.\n\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EImportant Information\u003C/b\u003E\u003Cp\u003EGuests are required to show a photo ID and credit card upon check-in. Please note that all Special Requests are subject to availability and additional charges may apply. Bookings on and beyond January 01, 2024 - A daily destination fee of $25.00 pretax (subject to change) is applied to each room of your stay in order to provide the following services and amenities, which enhance the guest experience. Please find below the services and experience: · Daily $25 Dining Credit for Lunch or Dinner in any of our outlets · Daily Premium Guest room Internet · Discounted Daily Parking · 10% Discount on Luxury Car Service through our preferred transportation provider · 20% Discount on apparel in Market Chicago · Discounted Access to Lake Shore Fitness · 15% discount on shoe shines provided by Spa Di Lafronza\u003C/p\u003E",
                "isRefundable": false,
                "isPartialRefundable": false,
                "cancellationPenaltyRate": "1.0",
                "ppnPropertyId": 700024973,
                "rateId": "66541893-fb54-0401-091b-1b7498fe8075",
                "baseRate": "317.74",
                "tax": "47.66",
                "otherFees": "29.35",
                "chargeAmount": "365.40",
                "strikeThroughPrice": "524.00",
                "displayCurrency": {
                    "USD": {
                    "baseRate": "317.74",
                    "tax": "47.66",
                    "chargeAmount": "365.40",
                    "otherFees": "29.35",
                    "strikeThroughPrice": "524.00"
                    },
                    "CAD": {
                    "baseRate": "434.35",
                    "tax": "65.15",
                    "chargeAmount": "499.51",
                    "otherFees": "40.12",
                    "strikeThroughPrice": "716.32"
                    },
                    "EUR": {
                    "baseRate": "292.88",
                    "tax": "43.93",
                    "chargeAmount": "336.82",
                    "otherFees": "27.05",
                    "strikeThroughPrice": "483.02"
                    },
                    "GBP": {
                    "baseRate": "249.51",
                    "tax": "37.43",
                    "chargeAmount": "286.94",
                    "otherFees": "23.05",
                    "strikeThroughPrice": "411.49"
                    },
                    "AUD": {
                    "baseRate": "479.76",
                    "tax": "71.96",
                    "chargeAmount": "551.73",
                    "otherFees": "44.32",
                    "strikeThroughPrice": "791.21"
                    }
                }
                }
            ],
            "beds": null,
            "roomImages": [
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/516312330.jpg?k=363d49c74a9dc4862bf04e44a36b28cd3ef1b0eb5d209d003f0cb72c1fc44b7e&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/516312330.jpg?k=363d49c74a9dc4862bf04e44a36b28cd3ef1b0eb5d209d003f0cb72c1fc44b7e&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/516312330.jpg?k=363d49c74a9dc4862bf04e44a36b28cd3ef1b0eb5d209d003f0cb72c1fc44b7e&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/488804287.jpg?k=80c254cba281b6ba699edc8979c62644e1f8f62dc6859e308911e649898ea54e&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/488804287.jpg?k=80c254cba281b6ba699edc8979c62644e1f8f62dc6859e308911e649898ea54e&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/488804287.jpg?k=80c254cba281b6ba699edc8979c62644e1f8f62dc6859e308911e649898ea54e&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/488804123.jpg?k=98b664e5e6510f06a78af39869cb81a4aaa34c12b4a45f543f3084dd00c79e0e&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/488804123.jpg?k=98b664e5e6510f06a78af39869cb81a4aaa34c12b4a45f543f3084dd00c79e0e&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/488804123.jpg?k=98b664e5e6510f06a78af39869cb81a4aaa34c12b4a45f543f3084dd00c79e0e&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/488804285.jpg?k=89bf55c455778d2914119a9e68617e1f8e475d93278f27daf3d0fc6a015351d1&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/488804285.jpg?k=89bf55c455778d2914119a9e68617e1f8e475d93278f27daf3d0fc6a015351d1&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/488804285.jpg?k=89bf55c455778d2914119a9e68617e1f8e475d93278f27daf3d0fc6a015351d1&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/488804542.jpg?k=927df5d062c43388e2570d65be3dc715daf179f5d4e0a3cb4d3f8ba09d218d07&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/488804542.jpg?k=927df5d062c43388e2570d65be3dc715daf179f5d4e0a3cb4d3f8ba09d218d07&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/488804542.jpg?k=927df5d062c43388e2570d65be3dc715daf179f5d4e0a3cb4d3f8ba09d218d07&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/488804487.jpg?k=7a6cfe4428d0b82dabf3a479c2e6241ebd3f1f73b029717273824a84f4d5561f&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/488804487.jpg?k=7a6cfe4428d0b82dabf3a479c2e6241ebd3f1f73b029717273824a84f4d5561f&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/488804487.jpg?k=7a6cfe4428d0b82dabf3a479c2e6241ebd3f1f73b029717273824a84f4d5561f&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/488804648.jpg?k=d0a3dd56f5bc0a089ed9792bdae248b1e0f8c72fc1989f4686f21893492e75e8&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/488804648.jpg?k=d0a3dd56f5bc0a089ed9792bdae248b1e0f8c72fc1989f4686f21893492e75e8&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/488804648.jpg?k=d0a3dd56f5bc0a089ed9792bdae248b1e0f8c72fc1989f4686f21893492e75e8&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/516312361.jpg?k=51c4d99f6d59c80db5f955b605b1aefdc62b5a79ea5028d08f7078352255996c&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/516312361.jpg?k=51c4d99f6d59c80db5f955b605b1aefdc62b5a79ea5028d08f7078352255996c&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/516312361.jpg?k=51c4d99f6d59c80db5f955b605b1aefdc62b5a79ea5028d08f7078352255996c&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/516312411.jpg?k=a4803aa71769b8755706554fd545fdb34d486583883f966ebbcaed6d8f72ef9e&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/516312411.jpg?k=a4803aa71769b8755706554fd545fdb34d486583883f966ebbcaed6d8f72ef9e&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/516312411.jpg?k=a4803aa71769b8755706554fd545fdb34d486583883f966ebbcaed6d8f72ef9e&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/516202048.jpg?k=a7c95746980100b2cadb3720af2690db66f2aab68fdb9ca5661688d313a90e3d&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/516202048.jpg?k=a7c95746980100b2cadb3720af2690db66f2aab68fdb9ca5661688d313a90e3d&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/516202048.jpg?k=a7c95746980100b2cadb3720af2690db66f2aab68fdb9ca5661688d313a90e3d&o="
                }
            ],
            "facilities": [],
            "top_facilities": []
            },
            {
            "code": "900103033",
            "name": "Skyline Junior Suite",
            "description": "This suite features a iPod dock, seating area and air conditioning.",
            "rates": [
                {
                "rateClass": "NRF",
                "rateType": "RECHECK",
                "allotment": 2,
                "paymentType": "AT_WEB",
                "packaging": false,
                "boardCode": "RO",
                "cancellationPolicies": [
                    {
                    "from": "2020-08-29T17:00:00-05:00",
                    "penaltyAmount": "535.03",
                    "displayCurrency": {
                        "USD": {
                        "penaltyAmount": "535.03"
                        },
                        "CAD": {
                        "penaltyAmount": "731.39"
                        },
                        "EUR": {
                        "penaltyAmount": "493.18"
                        },
                        "GBP": {
                        "penaltyAmount": "420.15"
                        },
                        "AUD": {
                        "penaltyAmount": "807.86"
                        }
                    }
                    }
                ],
                "rooms": 1,
                "adults": 2,
                "children": 0,
                "cancellationPolicy": "\u003Cb\u003ECancellation Policy\u003C/b\u003E\u003Cp\u003EIf you do not check in to the hotel on the first day of your reservation and do not alert the hotel in advance, the hotel reserves the right to cancel your reservation and you may be charged for the full amount.\u003C/p\u003E",
                "rateComments": "\u003Cb\u003ECancellation Policy\u003C/b\u003E\u003Cp\u003EIf you do not check in to the hotel on the first day of your reservation and do not alert the hotel in advance, the hotel reserves the right to cancel your reservation and you may be charged for the full amount.\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003ERefund Policy\u003C/b\u003E\u003Cp\u003EAny cancellation received within 2 days prior to arrival date will incur the first night charge. Failure to arrive at your hotel or property will be treated as a No-Show and no refund will be given (Property policy).\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EPhoto Policy\u003C/b\u003E\u003Cp\u003EThe reservation holder must present a valid photo ID and credit card at check-in. The credit card is required for \u003Cb\u003Ethe mandatory fee listed above as well as\u003C/b\u003E any additional hotel incidental charges such as parking, phone calls or minibar charges which are not included in the room rate.\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EPromo has been applied\u003C/b\u003E\u003Cp\u003E\u003Cb\u003ENegotiated Special Details:\u003C/b\u003E\u003Cli\u003E\u003Cem\u003EOn Sale Now -\u003E Save 10% on this stay\u003C/em\u003E&nbsp;&#151;&nbsp;Book Now and Save\u003C/li\u003E\u003Cli\u003EOffer Details:&nbsp;Negotiated Specials may be limited to certain dates and subject to availability.\u003C/li\u003E\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003ERate Description\u003C/b\u003E\u003Cp\u003ESpecial Rate\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EHotel Occupancy Policy\u003C/b\u003E\u003Cp\u003EAll rooms booked for triple occupancy (i.e. 3 adults). Accommodations for more than this are not guaranteed.\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003ERoom Charge Disclosure\u003C/b\u003E\u003Cp\u003EYour credit card is charged the total cost at time of purchase. Prices and room availability are not guaranteed until full payment is received.\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EHotel Pet Policy\u003C/b\u003E\u003Cp\u003EPets are not allowed.\n\u003C/p\u003E\u003Cbr\u003E\u003Cb\u003EImportant Information\u003C/b\u003E\u003Cp\u003EGuests are required to show a photo ID and credit card upon check-in. Please note that all Special Requests are subject to availability and additional charges may apply. Bookings on and beyond January 01, 2024 - A daily destination fee of $25.00 pretax (subject to change) is applied to each room of your stay in order to provide the following services and amenities, which enhance the guest experience. Please find below the services and experience: · Daily $25 Dining Credit for Lunch or Dinner in any of our outlets · Daily Premium Guest room Internet · Discounted Daily Parking · 10% Discount on Luxury Car Service through our preferred transportation provider · 20% Discount on apparel in Market Chicago · Discounted Access to Lake Shore Fitness · 15% discount on shoe shines provided by Spa Di Lafronza\u003C/p\u003E",
                "isRefundable": false,
                "isPartialRefundable": false,
                "cancellationPenaltyRate": "1.0",
                "ppnPropertyId": 700024973,
                "rateId": "66541893-fb57-0401-904f-eb475b2607e0",
                "baseRate": "465.24",
                "tax": "69.79",
                "otherFees": "29.35",
                "chargeAmount": "535.03",
                "strikeThroughPrice": "524.00",
                "displayCurrency": {
                    "USD": {
                    "baseRate": "465.24",
                    "tax": "69.79",
                    "chargeAmount": "535.03",
                    "otherFees": "29.35",
                    "strikeThroughPrice": "524.00"
                    },
                    "CAD": {
                    "baseRate": "635.99",
                    "tax": "95.40",
                    "chargeAmount": "731.39",
                    "otherFees": "40.12",
                    "strikeThroughPrice": "716.32"
                    },
                    "EUR": {
                    "baseRate": "428.85",
                    "tax": "64.33",
                    "chargeAmount": "493.18",
                    "otherFees": "27.05",
                    "strikeThroughPrice": "483.02"
                    },
                    "GBP": {
                    "baseRate": "365.35",
                    "tax": "54.80",
                    "chargeAmount": "420.15",
                    "otherFees": "23.05",
                    "strikeThroughPrice": "411.49"
                    },
                    "AUD": {
                    "baseRate": "702.48",
                    "tax": "105.37",
                    "chargeAmount": "807.86",
                    "otherFees": "44.32",
                    "strikeThroughPrice": "791.21"
                    }
                }
                }
            ],
            "beds": null,
            "roomImages": [
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/206614524.jpg?k=19c435444998e5839d045583ef421c26c53bddf98a4598b52e13ff819ad0331b&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/206614524.jpg?k=19c435444998e5839d045583ef421c26c53bddf98a4598b52e13ff819ad0331b&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/206614524.jpg?k=19c435444998e5839d045583ef421c26c53bddf98a4598b52e13ff819ad0331b&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/206614593.jpg?k=201e2eebf5aaa95b2cc6b81bbd86251da636673b24bb95bc7beef47c2ce4c05e&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/206614593.jpg?k=201e2eebf5aaa95b2cc6b81bbd86251da636673b24bb95bc7beef47c2ce4c05e&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/206614593.jpg?k=201e2eebf5aaa95b2cc6b81bbd86251da636673b24bb95bc7beef47c2ce4c05e&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/206614081.jpg?k=1f7f767381cf2c864658e2061280450aeea5ac4d0a77b64578cd91b7822f2950&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/206614081.jpg?k=1f7f767381cf2c864658e2061280450aeea5ac4d0a77b64578cd91b7822f2950&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/206614081.jpg?k=1f7f767381cf2c864658e2061280450aeea5ac4d0a77b64578cd91b7822f2950&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/206614164.jpg?k=dfa6bcd3ea2c0e2568b5b68a9af2b34644dc893cf0586d24dda324f58be0b5ce&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/206614164.jpg?k=dfa6bcd3ea2c0e2568b5b68a9af2b34644dc893cf0586d24dda324f58be0b5ce&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/206614164.jpg?k=dfa6bcd3ea2c0e2568b5b68a9af2b34644dc893cf0586d24dda324f58be0b5ce&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/206614607.jpg?k=9e57ffa7320ea454f0c84e36f2b3fb77eaaa675eb91979d557651b0200cf0f63&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/206614607.jpg?k=9e57ffa7320ea454f0c84e36f2b3fb77eaaa675eb91979d557651b0200cf0f63&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/206614607.jpg?k=9e57ffa7320ea454f0c84e36f2b3fb77eaaa675eb91979d557651b0200cf0f63&o="
                },
                {
                "description": null,
                "smallUrl": "//q-xx.bstatic.com/xdata/images/hotel/square60/206614481.jpg?k=86903c5400424539b7392d52d99680af1f558f9f0b10092e2e37afbb55ba3fde&o=",
                "mediumUrl": "//q-xx.bstatic.com/xdata/images/hotel/max300/206614481.jpg?k=86903c5400424539b7392d52d99680af1f558f9f0b10092e2e37afbb55ba3fde&o=",
                "largeUrl": "//q-xx.bstatic.com/xdata/images/hotel/max500/206614481.jpg?k=86903c5400424539b7392d52d99680af1f558f9f0b10092e2e37afbb55ba3fde&o="
                }
            ],
            "facilities": [],
            "top_facilities": []
            }
        ],
        "destination_code": "ORD",
        "avg_min_price": 164.9,
        "additional_info": {
            "checkin_24_hour": null,
            "checkin_begin_time": "6:00 PM",
            "checkin_end_time": "midnight",
            "checkin_instructions": "\u003Cul\u003E  \u003Cli\u003EExtra-person charges may apply and vary depending on property policy\u003C/li\u003E\u003Cli\u003EGovernment-issued photo identification and a credit card, debit card, or cash deposit may be required at check-in for incidental charges\u003C/li\u003E\u003Cli\u003ESpecial requests are subject to availability upon check-in and may incur additional charges; special requests cannot be guaranteed\u003C/li\u003E\u003Cli\u003ESpecial cancellation policies or charges may apply for group reservations (more than 8 rooms for the same property / stay dates)\u003C/li\u003E\u003Cli\u003ESafety features at this property include a carbon monoxide detector, a fire extinguisher, a smoke detector, a security system, a first aid kit, and window guards\u003C/li\u003E\u003Cli\u003EBe prepared: check the latest COVID-19 travel requirements and measures in place for this destination before you travel.\u003C/li\u003E\u003Cli\u003EPlease note that cultural norms and guest policies may differ by country and by property; the policies listed are provided by the property\u003C/li\u003E  \u003C/ul\u003E \u003Cul\u003E  \u003Cli\u003EIt is Hyatt’s practice to enter any occupied guestroom at a minimum of once within a 24-hour period, even if a guest has requested privacy.  Appropriate efforts are made to provide advance notice to the registered guest before entering an occupied guestroom.\u003C/li\u003E  \u003C/ul\u003E",
            "checkin_special_instructions": "Front desk staff will greet guests on arrival.  This property accepts only chip-and-PIN credit and debit cards for onsite payments.",
            "checkin_min_age": 21,
            "checkout_time": "11:00 AM",
            "fees_mandatory": "\u003Cp\u003EYou'll be asked to pay the following charges at the property:\u003C/p\u003E \u003Cul\u003E\u003Cli\u003EBreakage deposit: USD 100 per stay\u003C/li\u003E\u003C/ul\u003E \u003Cp\u003EWe have included all charges provided to us by the property. \u003C/p\u003E",
            "fees_optional": "\u003Cul\u003E \u003Cli\u003EFee for buffet breakfast: approximately USD 15.00–24.50 for adults, and USD 10.00–15.00 for children\u003C/li\u003E        \u003Cli\u003ECovered valet parking fee: USD 79 per night (in/out privileges)\u003C/li\u003E  \u003Cli\u003ENearby parking fee: USD 65 per day (160 ft away)\u003C/li\u003E        \u003Cli\u003ERollaway bed fee: USD 25.0 per stay\u003C/li\u003E            \u003C/ul\u003E \u003Cp\u003EThe above list may not be comprehensive. Fees and deposits may not include tax and are subject to change. \u003C/p\u003E",
            "descriptions_headline": "Near Millennium Park",
            "descriptions_rooms": "Make yourself at home in one of the 2032 guestrooms featuring iPod docking stations and flat-screen televisions. Your pillowtop bed comes with premium bedding. Complimentary wired and wireless Internet access keeps you connected, and digital programming provides entertainment. Private bathrooms have designer toiletries and hair dryers.",
            "guest_rating_count": 2307,
            "guest_rating_overall": "4.3",
            "guest_rating_cleanliness": "4.3",
            "guest_rating_service": "4.4",
            "guest_rating_comfort": "4.3",
            "guest_rating_condition": "4.2",
            "guest_rating_location": null,
            "guest_rating_neighborhood": null,
            "guest_rating_quality": null,
            "guest_rating_value": null,
            "guest_rating_amenities": "4.1",
            "guest_rating_recommendation_percent": null,
            "tripadvisor_rating": null
        },
        "full_address": "151 E Wacker Dr Chicago, Chicago, Illinois, IL, United States, US, 60601",
        "primary_region_id": 829,
        "dist_to_primary_region": 1.25874433403,
        "hp_hotel_id": null,
        "check_in_time_range": {
            "start": "18:00:00",
            "end": "00:00:00"
        },
        "check_out_time_range": {
            "start": "12:00:00",
            "end": "11:00:00"
        },
        "minrate": null,
        "currency": "USD",
        "minRoomRate": {
            "roomIdx": 0,
            "rateIdx": 0,
            "rateId": "66541893-fb44-0401-517d-5300af160108"
        },
        "externalLinks": {
            "booking.com": {
            "link": "https://www.booking.com/searchresults.html?aid=1278861&landmark=20033173&highlighted_hotels=46687&checkin=2024-05-26&checkout=2024-05-27&label=v3|20240526|20240527|65741||||hotels-4ce8cdb0fa2d|PUB|6650c5294fdda092f260f4bafa2ced4b||mobytrip",
            "baseRate": "230.00",
            "tax": "44.37",
            "otherFees": "25.00",
            "roomId": 4668726,
            "roomName": "Queen Room",
            "roomDescription": "This room includes a coffee machine and private bathroom with a shower.",
            "blockId": "4668726_263833354_2_2_0",
            "currencyCode": "USD",
            "tzShift": null,
            "chargeCurrency": "AT_HOTEL",
            "isRefundable": false,
            "refundableUntil": null,
            "isBreakfastIncluded": false,
            "boardCode": "RO",
            "click_id": "66541894-11e8-0201-0f95-5b02d14037cc",
            "displayCurrency": {
                "USD": {
                "baseRate": "230.00",
                "tax": "44.37",
                "chargeAmount": "274.37",
                "otherFees": "25.00"
                },
                "CAD": {
                "baseRate": "314.42",
                "tax": "60.65",
                "chargeAmount": "375.07",
                "otherFees": "34.18"
                },
                "EUR": {
                "baseRate": "212.01",
                "tax": "40.90",
                "chargeAmount": "252.91",
                "otherFees": "23.04"
                },
                "GBP": {
                "baseRate": "180.62",
                "tax": "34.84",
                "chargeAmount": "215.46",
                "otherFees": "19.63"
                },
                "AUD": {
                "baseRate": "347.29",
                "tax": "67.00",
                "chargeAmount": "414.28",
                "otherFees": "37.75"
                }
            }
            }
        },
        "garPropertyId": null,
        "hpPropertyId": null,
        "is_available": true
    }
    hotel_s = HotelSerializer(data=j)
    hotel_s.is_valid()
    update_dict = {"info":j}
    hotel_s.validated_data.update(**update_dict)
    hotel = hotel_s.save()

    for room_j in j["rooms"]:
        room_s = RoomSerializer(data=room_j)
        room_s.is_valid()
        update_dict = {"hotel":hotel}
        room_s.validated_data.update(**update_dict)
        room = room_s.save()
        hotel.rooms.add(room)

        for rate_j in room_j["rates"]:
            rate_s = RateSerializer(data=rate_j)
            rate_s.is_valid()
            update_dict = {"room":room}
            rate_s.validated_data.update(**update_dict)
            rate = rate_s.save()
            room.rates.add(rate)

    print("==========> init completed")
    return hotel
