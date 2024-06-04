import { ref, computed } from "vue"
import { defineStore } from "pinia"
import axios from 'axios'

export const useFinanceStore = defineStore("finance", () => {
  const BASE_URL = 'http://127.0.0.1:8000'

  const deposits = ref([])
  const savings = ref([])

  const periods = [1, 3, 6, 12, 24, 36]
  const depositBanks = ref([])
  const savingBanks = ref([])
  
  const getProducts = function () {
    axios({
      method: 'get',
      url: `${BASE_URL}/finance/products/get_product/`,
    })
      .then(res => {
        let i = 0
        while (i < res.data.length) {
          if (res.data[i].category === 0) {
            if (!depositBanks.value.includes(res.data[i].kor_co_nm)) {
              depositBanks.value.push(res.data[i].kor_co_nm)
            }
            const deposit = ref(res.data[i])
            const rates = ref([])
            for (let j=0; j<6; j++) {
              rates.value.push(res.data[i].intr_rate)
              rates.value.push(res.data[i].intr_rate2)
              i++
            }
            deposit.value.rates = rates.value
            deposits.value.push(deposit.value)
          } else {
            if (!savingBanks.value.includes(res.data[i].kor_co_nm)) {
              savingBanks.value.push(res.data[i].kor_co_nm)
            }
            const saving = ref(res.data[i])
            const rates = ref([])
            for (let j=0; j<6; j++) {
              rates.value.push(res.data[i].intr_rate)
              rates.value.push(res.data[i].intr_rate2)
              i++
            }
            saving.value.rates = rates.value
            savings.value.push(saving.value)
          }
        }
      })
      .catch(err => console.log(err))
  }
  return { BASE_URL, getProducts, deposits, savings, periods, depositBanks, savingBanks };
}, { persist: true })
