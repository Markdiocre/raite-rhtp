import { ref, onMounted, onUnmounted } from 'vue'
import axios from 'axios'
const baseURL = 'http://127.0.0.1:8000/api/v1'
const jwt = ref<string>('')

export function GetToken() {
  return jwt.value
}

export function SetToken(newToken: string) {
  jwt.value = newToken
}

export function Login(email: string, password: string) {
  return axios
    .post(`${baseURL}/auth/token/login/`, {
      email,
      password
    })
    .then((data: any) => {
      jwt.value = data.auth_token
      console.log('success on logging in')
      return true
    })
    .catch((err) => {
      console.log(err)
      console.log('failed to login')
      return false
    })
}

export function Register(
  first_name: string,
  last_name: string,
  middle_name: string,
  phone_number: number | undefined,
  address: string,
  gender: string,
  email: string,
  password: string,
  role: string
) {
  gender = gender.toUpperCase()
  return axios
    .post(`${baseURL}/auth/users/`, {
      first_name,
      last_name,
      middle_name,
      phone_number,
      address,
      gender,
      email,
      password,
      role
    })
    .then(() => {
      console.log('success on creating a account')
      return true
    })
    .catch((err) => {
      console.log(axios.defaults.baseURL)
      console.log(err)

      console.log('failed to create account')
      return false
    })
}
export function Logout() {
  const isLogout = axios
    .post(`${baseURL}/auth/token/logout/`)
    .then(() => {
      return true
    })
    .catch((err) => {
      return false
    })
  jwt.value = ''
  return isLogout
}
