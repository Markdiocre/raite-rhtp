import { ref, onMounted, onUnmounted } from 'vue'
import axios from 'axios'
import { GetToken } from './auth'

export async function GetProviderAvail() {
  const data = axios
    .get('http://127.0.0.1:8000/api/v1/show/providers/', {
      headers: { Authorization: GetToken() }
    })
    .then((data) => {
      console.log(data)
    })
}
