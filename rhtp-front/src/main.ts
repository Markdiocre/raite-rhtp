import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import './style.css'
axios.defaults.baseURL = 'http://127.0.0.1:8000/api/v1/'
// import.meta.env.VITE_APP_STATUS == 'LOCAL'
// ? import.meta.env.VITE_API_LOCAL_URL
// : import.meta.env.VITE_API_DEPLOYMENT_URL

const app = createApp(App)

app.use(router)

app.mount('#app')
