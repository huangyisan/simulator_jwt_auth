import axios from 'axios'

import router from '../router'


export function request(config) {
  const token = sessionStorage.getItem('token')
  const instance = axios.create({
    // baseURL: 'http://mall.kirakirazone.com',
    baseURL: 'http://127.0.0.1:8000',
    timeout: 5000,
    headers: {
      'Authorization': 'Bearer ' + token,
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })


  instance.interceptors.response.use(res => {
    const code = res.data.code
    console.log(document.location)
    console.log(res)
    if (code === 401 && document.location.pathname !== '/login') {
      console.log('登陆失败或失效')
      sessionStorage.removeItem('token')
      router.push('/login')
      return res.data
    } else if (code === 401 && document.location.pathname === '/login') {
      // console.log('不跳转了')
      // return false
      return res.data
    }
    return res.data
  })

  return instance(config)
}