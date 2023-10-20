<script setup lang="ts">
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { ref } from 'vue'
import { Register } from '@/Composables/auth'

const router = useRouter()

const email = ref<string>('')
const password = ref<string>('')
const role = ref<string>('Pick one')
const fName = ref<string>('')
const mName = ref<string>('')
const lName = ref<string>('')
const birthDate = ref<Date>()
const gender = ref<string>('Pick one')
const phoneNumber = ref<number>()
const address = ref<string>('')

async function RegisterSubmit() {
  console.log(`1${fName.value}
    2${lName.value}
    3${mName.value}
    4${phoneNumber.value}
    5${address.value}
    6${gender.value}
    7${email.value}
    8${password.value}
    9${role.value}`)
  const isRegister: any = await Register(
    fName.value,
    lName.value,
    mName.value,
    phoneNumber.value,
    address.value,
    gender.value,
    email.value,
    password.value,
    role.value
  )

  if (isRegister == true) {
    router.push({
      name: 'login'
    })
  }
}
</script>

<template>
  <div class="justify-center flex">
    <div class="card w-96 bg-primary text-primary-content justify">
      <div class="card-body">
        <h2 class="card-title">Register</h2>
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
        <div class="form-control w-full max-w-xs">
          <label class="label">
            <span class="label-text">Role</span>
          </label>
          <select class="select select-bordered" v-model="role">
            <option disabled selected>Pick one</option>
            <option>patient</option>
            <option>provider</option>
          </select>
        </div>
        <div class="form-control w-full max-w-xs">
          <label class="label">
            <span class="label-text">First name</span>
          </label>
          <input
            type="text"
            placeholder="Type here"
            class="input input-bordered w-full max-w-xs"
            v-model="fName"
          />
        </div>
        <div class="form-control w-full max-w-xs">
          <label class="label">
            <span class="label-text">Middle name</span>
          </label>
          <input
            type="text"
            placeholder="Type here"
            class="input input-bordered w-full max-w-xs"
            v-model="mName"
          />
        </div>
        <div class="form-control w-full max-w-xs">
          <label class="label">
            <span class="label-text">Last Name</span>
          </label>
          <input
            type="text"
            placeholder="Type here"
            class="input input-bordered w-full max-w-xs"
            v-model="lName"
          />
        </div>
        <div class="form-control w-full max-w-xs">
          <label class="label">
            <span class="label-text">Birth date</span>
          </label>
          <input
            type="date"
            placeholder="Type here"
            class="input input-bordered w-full max-w-xs"
            v-model="birthDate"
          />
        </div>
        <div class="form-control w-full max-w-xs">
          <label class="label">
            <span class="label-text">Gender</span>
          </label>
          <select class="select select-bordered" v-model="gender">
            <option disabled selected>Pick one</option>
            <option>Male</option>
            <option>Female</option>
            <option>Other</option>
          </select>
          <div class="form-control w-full max-w-xs">
            <label class="label">
              <span class="label-text">Phone Number</span>
            </label>
            <input
              type="tel"
              placeholder="Type here"
              class="input input-bordered w-full max-w-xs"
              v-model="phoneNumber"
            />
          </div>
        </div>
        <div class="form-control">
          <label class="label">
            <span class="label-text">Your Address</span>
          </label>
          <textarea
            class="textarea textarea-bordered h-24"
            placeholder="Type here"
            v-model="address"
          ></textarea>
        </div>

        <div class="card-actions justify-between">
          <RouterLink class="btn btn-primary" to="/login">Login</RouterLink>
          <button class="btn" @click="RegisterSubmit">Register</button>
        </div>
      </div>
    </div>
  </div>
</template>
