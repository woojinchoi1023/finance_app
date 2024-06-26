<template>
  <v-container>
    <v-col class="mb-4">
      <span class="text-h4">Map</span>
    </v-col>
    <div class="d-flex justify-start w-75">
      <v-select v-model="selectCity" :items="cities" density="compact"> </v-select>
      <v-select v-model="selectSubCity" :items="subCities[selectCity]" class="mx-5" density="compact">
      </v-select>
      <v-select v-model="place" :items="places.map((element) => element.place_name)" class="mx-5" density="compact">
      </v-select>
    </div>
    <v-container>
      <v-row>
        <v-col id="map" cols="6"></v-col>
        <v-col v-if="place.length > 0" class="mx-5" cols="5">
          <h2 class="mb-3">{{ placeInfo[0].place_name }}</h2>
          <h3 class="mb-2">상세정보</h3>
          <p class="mb-1"><strong>주소</strong> : {{ placeInfo[0].road_address_name }}</p>
          <p><strong>전화번호</strong> : {{ placeInfo[0].phone }}</p>
        </v-col>
      </v-row>
    </v-container>
  </v-container>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";

const selectCity = ref("서울특별시");
const selectSubCity = ref("");
const places = ref([]);
const place = ref("");
const placeInfo = ref("");

const cities = ref([
  "강원특별자치도",
  "경기도",
  "경상남도",
  "경상북도",
  "광주광역시",
  "대구광역시",
  "대전광역시",
  "부산광역시",
  "세종특별자치시",
  "울산광역시",
  "인천광역시",
  "전라남도",
  "전북특별자치도",
  "제주특별자치도",
  "충청남도",
  "충청북도",
]);

const subCities = ref({
  강원특별자치도: [
    "강릉시",
    "고성군",
    "동해시",
    "삼척시",
    "속초시",
    "양구군",
    "양양군",
    "영월군",
    "원주시",
    "인제군",
    "정선군",
    "철원군",
    "춘천시",
    "태백시",
    "평창군",
    "홍천군",
    "화천군",
    "횡성군",
  ],
  경기도: [
    "가평군",
    "고양시",
    "과천시",
    "광명시",
    "광주시",
    "구리시",
    "군포시",
    "김포시",
    "남양주시",
    "동두천시",
    "부천시",
    "성남시",
    "수원시",
    "시흥시",
    "안산시",
    "안성시",
    "안양시",
    "양주시",
    "양평군",
    "여주시",
    "연천군",
    "오산시",
    "용인시",
    "의왕시",
    "의정부시",
    "이천시",
    "파주시",
    "평택시",
    "포천시",
    "하남시",
    "화성시",
  ],
  경상남도: [
    "거제시",
    "거창군",
    "고성군",
    "김해시",
    "남해군",
    "밀양시",
    "사천시",
    "산청군",
    "양산시",
    "의령군",
    "진주시",
    "창녕군",
    "창원시",
    "통영시",
    "하동군",
    "함안군",
    "함양군",
    "합천군",
  ],
  경상북도: [
    "경산시",
    "경상북도",
    "경주시",
    "고령군",
    "구미시",
    "김천시",
    "문경시",
    "봉화군",
    "상주시",
    "성주군",
    "안동시",
    "영덕군",
    "영양군",
    "영주시",
    "영천시",
    "예천군",
    "울릉군",
    "울진군",
    "의성군",
    "청도군",
    "청송군",
    "칠곡군",
    "포항시",
  ],
  광주광역시: ["광산구", "남구", "동구", "북구", "서구"],
  대구광역시: [
    "군위군",
    "남구",
    "달서구",
    "달성군",
    "대구광역시",
    "동구",
    "북구",
    "서구",
    "수성구",
    "중구",
  ],
  대전광역시: ["대덕구", "동구", "서구", "유성구", "중구"],
  부산광역시: [
    "강서구",
    "금정구",
    "기장군",
    "남구",
    "동구",
    "동래구",
    "부산진구",
    "북구",
    "사상구",
    "사하구",
    "서구",
    "수영구",
    "연제구",
    "영도구",
    "중구",
    "해운대구",
  ],
  서울특별시: [
    "강남구",
    "강동구",
    "강북구",
    "강서구",
    "관악구",
    "광진구",
    "구로구",
    "금천구",
    "노원구",
    "도봉구",
    "동대문구",
    "동작구",
    "마포구",
    "서대문구",
    "서초구",
    "성동구",
    "성북구",
    "송파구",
    "양천구",
    "영등포구",
    "용산구",
    "은평구",
    "종로구",
    "중구",
    "중랑구",
  ],
  세종특별자치시: [],
  울산광역시: ["남구", "동구", "북구", "울주군", "중구"],
  인천광역시: [
    "강화군",
    "계양구",
    "남동구",
    "동구",
    "미추홀구",
    "부평구",
    "서구",
    "연수구",
    "옹진군",
    "중구",
  ],
  전라남도: [
    "강진군",
    "고흥군",
    "곡성군",
    "광양시",
    "구례군",
    "나주시",
    "담양군",
    "목포시",
    "무안군",
    "보성군",
    "순천시",
    "신안군",
    "여수시",
    "영광군",
    "영암군",
    "완도군",
    "장성군",
    "장흥군",
    "진도군",
    "함평군",
    "해남군",
    "화순군",
  ],
  전북특별자치도: [
    "고창군",
    "군산시",
    "김제시",
    "남원시",
    "무주군",
    "부안군",
    "순창군",
    "완주군",
    "익산시",
    "임실군",
    "장수군",
    "전주시",
    "정읍시",
    "진안군",
  ],
  제주특별자치도: ["제주시", "서귀포시"],
  충청남도: [
    "계룡시",
    "공주시",
    "금산군",
    "논산시",
    "당진시",
    "보령시",
    "부여군",
    "서산시",
    "서천군",
    "아산시",
    "예산군",
    "천안시",
    "청양군",
    "태안군",
    "홍성군",
  ],
  충청북도: [
    "괴산군",
    "단양군",
    "보은군",
    "영동군",
    "옥천군",
    "음성군",
    "제천시",
    "증평군",
    "진천군",
    "청주시",
    "충주시",
  ],
});

let map;

const initializeMap = () => {
  const container = document.getElementById("map");
  const options = {
    center: new kakao.maps.LatLng(37.5665, 126.978), // 서울 중심 좌표
    level: 3,
  };
  map = new kakao.maps.Map(container, options);
};

const searchPlaces = () => {
  // if (!selectedBank.value || !selectedRegion.value) {
  //   alert("Please select both a bank and a region!")
  //   return
  // }

  let query;
  if (place.value.length === 0) {
    query = `${selectCity.value} ${selectSubCity.value} 은행`;
  } else {
    query = place.value;
  }

  if (
    typeof kakao === "undefined" ||
    typeof kakao.maps === "undefined" ||
    typeof kakao.maps.services === "undefined"
  ) {
    console.error("Kakao Maps API is not loaded yet.");
    return;
  }

  const ps = new kakao.maps.services.Places();
  ps.keywordSearch(query, (data, status, pagination) => {
    if (status === kakao.maps.services.Status.OK) {
      if (place.value.length === 0) {
        places.value = data;
      }
      displayPlaces(data);
    } else {
      alert("Search failed!");
    }
  });
};

const displayPlaces = (places) => {
  const bounds = new kakao.maps.LatLngBounds();
  for (let i = 0; i < places.length; i++) {
    const place = places[i];
    const markerPosition = new kakao.maps.LatLng(place.y, place.x);
    const marker = new kakao.maps.Marker({
      position: markerPosition,
    });
    marker.setMap(map);
    bounds.extend(markerPosition);
  }
  map.setBounds(bounds);
};

onMounted(() => {
  if (typeof kakao !== "undefined" && kakao.maps) {
    initializeMap();
  } else {
    console.error("Kakao Maps API failed to load.");
  }
});

watch(selectCity, (newValue) => {
  selectSubCity.value = "";
});

watch(selectSubCity, (newValue) => {
  place.value = "";
});

watch([selectCity, selectSubCity, place], ([newValue1, newValue2]) => {
  placeInfo.value = "";
  searchPlaces();
});

watch(place, (newValue) => {
  if (place.value.length > 0) {
    placeInfo.value = places.value.filter(
      (element) => element.place_name === place.value
    );
  }
});
</script>

<style scoped>
#map {
  width: 500px;
  height: 400px;
}
</style>
