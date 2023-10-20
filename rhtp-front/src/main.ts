import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

axios.defaults.baseURL =
  import.meta.env.VITE_APP_STATUS == 'LOCAL'
    ? import.meta.env.VITE_API_LOCAL_URL
    : import.meta.env.VITE_API_DEPLOYMENT_URL

const app = createApp(App)

app.use(router)

app.mount('#app')
