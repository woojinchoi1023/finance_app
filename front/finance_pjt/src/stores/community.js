import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import router from '../router'


export const useCommunityStore = defineStore("community", () => {
  const token = ref(null)
  const userInfo = ref(null)
  const userPk = ref(null) // export 안하는중

  const signUp = async (payload) => {
    const {username, password1, password2, 
      first_name, last_name, email, nickname } = payload
    await axios({
      method:'post',
      url:`http://127.0.0.1:8000/accounts/signup/`,
      data:{
        username, password1, password2
      }
    }).then(res=>{
      console.log('signed up!')
    })
    .catch(err=> console.log(err))
    
    // login
    await axios({
      method:'post',
      url:`http://127.0.0.1:8000/accounts/login/`,
      data:{
        username, password:password1
      }
    }).then(res=>{
      token.value = res.data.key
    }).catch(err=> {
      console.log(err)
    })

    // get userPk
    await axios({
      method:'get',
      url:'http://127.0.0.1:8000/accounts/user/',
      headers: {
        Authorization: `Token ${token.value}`,
      },
    }).then(res=>{
      userPk.value = res.data.pk
    })

    // update detail
    await axios({
      method:'put',
      url:`http://127.0.0.1:8000/accounts/${userPk.value}/`,
      headers: {
        Authorization: `Token ${token.value}`,
      },
      data: {
        first_name, last_name, email, nickname
      }
    }).then(res=>{
      console.log('detail update!')
      console.log(res)
    }).catch(err=>console.log(err))

    getUserInfo()
    await router.push({name:'home'})

  }

  const logIn = (payload) => {
    const {username, password} = payload
    axios({
      method:'post',
      url:`http://127.0.0.1:8000/accounts/login/`,
      data:{
        username, password
      }
    }).then(res=>{
      token.value = res.data.key
      getUserPk()
      router.push({name:'home'})
    }).catch(err=> {
      console.log(err)
      alert("로그인에 실패했습니다.");
    })
  }

  const getUserPk = () => {
    axios({
      method:'get',
      url:'http://127.0.0.1:8000/accounts/user/',
      headers: {
        Authorization: `Token ${token.value}`,
      },
    }).then(res=>{
      userPk.value = res.data.pk
      getUserInfo()
    })
  }

  const getUserInfo = () => {
    axios({
      method:'get',
      url:`http://127.0.0.1:8000/accounts/${userPk.value}/`,
      headers: {
        Authorization: `Token ${token.value}`,
      },
    }).then(res=>{
      userInfo.value = res.data
    })
  }

  const logOut = () => {
    axios({
      method:'post',
      url:`http://127.0.0.1:8000/accounts/logout/`,
    }).then(res=>{
      console.log(res, 'log out')
      token.value = null
      userInfo.value =null
      router.go(0)
    }).catch(err=> console.log(err))
  }

  const isLogin = computed(() => token.value? true : false)

  return { signUp, logIn, logOut, token, isLogin, userInfo  };
}, { persist: true });
