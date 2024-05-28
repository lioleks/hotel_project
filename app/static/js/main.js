const apiService = {
  async fetchData(url) {
    try {
      const response = await fetch(url);
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Failed to fetch data:', error);
      return null;
    }
  }
};

function extractIdFromURL(url) {
  const regex = /\/(\d+)(?=\/?$)/;
  const match = url.match(regex);
  if (match && match[1]) {
    return parseInt(match[1], 10);
  }
  return null;
}

const currentURL = window.location.href;
const id = extractIdFromURL(currentURL);

const CurrencyDropdown = {
  data() {
    return {
      currencies: ['USD', 'CAD', 'EUR', 'GBP', 'AUD'],
      selectedCurrency: 'USD'
    };
  },
  methods: {
    selectCurrency(currency) {
      this.selectedCurrency = currency;
    }
  },
  template: `
    <div class="nav-item dropdown">
      <button class="btn btn-light dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
        {{ selectedCurrency }}
      </button>
      <ul class="dropdown-menu dropdown-menu-light">
        <li v-for="currency in currencies" :key="currency">
          <a class="dropdown-item" href="#" @click.prevent="selectCurrency(currency)">{{ currency }}</a>
        </li>
      </ul>
    </div>
  `
};

const Gallery = {
  props: ['images'],
  mounted() {
    Fancybox.bind('[data-fancybox="gallery"]');
  },
  methods: {
    getImageClass(index) {
      if (index < 5) {
        return 'i' + (index + 1);
      } else {
        return 'd-none';
      }
    }
  },
  template: `
    <div class="hotel-gallery">
      <figure class="five-grid-gallery">
        <a v-for="(image, index) in images" :key="index" :data-src="image.fullsize_url" :class="getImageClass(index)">
          <img data-fancybox="gallery" :src="image.fullsize_url" />
        </a>
      </figure>
    </div>
  `
};

const HotelInfo = {
  props: ['hotelData'],
  template: `
    <div class="hotel-info">
      <span class="badge text-bg-info">{{ hotelData.accommodation_type_code }}</span>
      <div class="d-flex justify-content-between align-items-top">
        <div>
          <h1> {{ hotelData.hotel_name }} </h1>
        </div>
        <div class="text-end">
          <h1 class="price"> {{ hotelData.price }} </h1>
          <span>Per night</span>
        </div>
      </div>
      <div class="pt-2">
        <span> {{ hotelData.full_address }} </span>
        <div class="tags">
          <span class="badge text-bg-secondary me-1" v-for="(distance, neighborhood) in hotelData.neighborhood">{{ neighborhood }}</span>
        </div>
        <a href="#choose-room" class="btn btn-primary d-lg-none w-100 mt-4">Choose Room</a>
      </div>
      <div>
        <h3>Property Description</h3>
        <p>{{ hotelData.description }}</p>

        <h3>The Neighborhood</h3>
        <ul>
          <li v-for="(distance, neighborhood) in hotelData.neighborhood">{{ neighborhood }} → {{distance }}</li>
        </ul>

        <h3>Points Of Interest</h3>
        <ul>
          <li v-for="(distance, points_of_interest) in hotelData.points_of_interest">{{ points_of_interest }} → {{distance }}</li>
        </ul>

        <h3>Nearby Airports</h3>
        <ul>
          <li v-for="(distance, nearby_airports) in hotelData.nearby_airports">{{ nearby_airports }} → {{distance }}</li>
        </ul>

        <h3>Facilities</h3>
        <h6>Check In Details</h6>
        <ul>
          <li>Check-in time: {{ hotelData.check_in_time_range }} </li>
          <li>Check-out time: {{ hotelData.check_out_time_range }} </li>
        </ul>
      </div>
    </div>
  `
};


const Rooms = {
  props: ['rooms'],
  methods: {
  },
  template: `
    <section class="room mt-3" v-for="room in rooms" :key="room.id">
    <div class="row">
        <div class="col-8">
            <h5>{{ room['description'] }}</h5>
            <h5 class="d-flex align-items-center">2<i class="icon-man"></i>&nbsp0<i class="icon-man icon-child"></i></h5>
            <p>Details <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0Z"></path></svg></p>
            <span class="badge text-bg-info">Free Wifi</span>
        </div>
        <div class="col-4 text-end">
            <h3>{{ room.price }}</h3>
            <p>per night</p>
            <h4>{{ room.total_price }}</h4>
            <p>(including taxes)</p>
        </div>
    </div>
    <button type="button" class="btn btn-primary w-100 mt-2">Reserve</button>
    </section>
  `
};

const HotelRatings = {
  props: ['hotelRatings'],
  template: `
  <h3>Ratings</h3>

  <div class="d-flex align-items-center gap-3">
      <div class="overall_rating_box"><span>4.3</span></div>
      <h5 class="overall_rating_description">Very good</h5>
      <h5 class="overall_rating_description">2307 ratings</h5>
  </div>
  <div v-for="(name, rating) in hotelRatings">
    <label>{{ name }}</label>
    qwe
  </div>
  `
}


const app = Vue.createApp({
  data() {
    return {
      images: [],
      hotelData: [],
      hotelRatings: [],
      roomsData: [],
    };
  },
  components: {
    'currency-dropdown' : CurrencyDropdown,
    'gallery' : Gallery,
    'hotel-info' : HotelInfo,
    'hotel-ratings' : HotelRatings,
    'hotel-rooms' : Rooms,
  },
  methods: {
    convertTime(timeString) {
      const [hours, minutes, seconds] = timeString.split(':').map(Number);
      const period = hours >= 12 ? 'pm' : 'am';
  
      const hours12 = hours % 12 || 12;
  
      const formattedTime = `${hours12}:${String(minutes).padStart(2, '0')} ${period}`;
  
      return formattedTime;
    }      
  },
  async mounted() {
    try {
      const hotel = await apiService.fetchData('/api/hotels/65741');
      this.roomsData  = await apiService.fetchData('/api/rooms/'+id);

      this.images = hotel['info']['images'];

      console.log(id);


      // Hotel data
      this.hotelData.accommodation_type_code = hotel['info']['accommodation_type_code'];
      this.hotelData.hotel_name = hotel['name'];
      this.hotelData.description = hotel['info']['description'];
      this.hotelData.hotel_code = hotel['info']['code'];
      this.hotelData.avg_min_price = hotel['info']['price'];
      this.hotelData.neighborhood = hotel['info']['neighborhood'];
      this.hotelData.points_of_interest = hotel['info']['points_of_interest'];
      this.hotelData.nearby_airports = hotel['info']['nearby_airports'];

      this.hotelData.check_in_time_range = this.convertTime(hotel['info']['check_in_time_range']['start'])
      + ' — ' + this.convertTime(hotel['info']['check_in_time_range']['end']);

      this.hotelData.check_out_time_range = this.convertTime(hotel['info']['check_out_time_range']['start'])
      + ' — ' + this.convertTime(hotel['info']['check_out_time_range']['end']);
      
      // Rating 
      this.hotelRatings = [
        {'Amenities' : hotel['info']['guest_rating_amenities']},
        {'Cleanliness' : hotel['info']['guest_rating_cleanliness']},
        {'Comfort' : hotel['info']['guest_rating_comfort']},
        {'Condition' : hotel['info']['guest_rating_condition']},
        {'Overall' : hotel['info']['guest_rating_overall']},
        {'Service' : hotel['info']['guest_rating_service']},
      ];

      }
    catch (error) {
      console.error('Error fetching data:', error);
    }
  }
});

app.mount('#app');

const map = L.map('map').setView([51.505, -0.09], 12);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.marker([51.5, -0.09]).addTo(map)
  .bindPopup('This hotel')
  .openPopup();
