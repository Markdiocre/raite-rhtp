<script setup lang="ts">
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { ref } from 'vue'
import { Login } from '@/Composables/auth'

const router = useRouter()

const email = ref<string>('')
const password = ref<string>('')

async function LoginSubmit() {
  console.log(`email: ${email.value}\npassword: ${password.value}`)
  Login(email.value, password.value)
  // console.log(`status login ${isLogin}`)
}
</script>

<template>
  <div class="flex justify-center">
    <div class="card w-96 bg-primary text-primary-content justify">
      <div class="card-body">
        <h2 class="card-title">Login</h2>
        <div class="form-control w-full max-w-xs">
          <label class="label">
            <span class="label-text">Email</span>
          </label>
          <input
            type="Email"
            placeholder="Type here"
            class="input input-bordered w-full max-w-xs"
            v-model="email"
          />
        </div>
        <div class="form-control w-full max-w-xs">
          <label class="label">
            <span class="label-text">Password</span>
          </label>
          <input
            type="password"
            placeholder="Type here"
            class="input input-bordered w-full max-w-xs"
            v-model="password"
          />
        </div>
        <div class="card-actions justify-between">
          <RouterLink class="btn btn-primary" to="/register">Register</RouterLink>
          <button class="btn" @click="LoginSubmit()">Login</button>
        </div>
      </div>
    </div>
  </div>
</template>
