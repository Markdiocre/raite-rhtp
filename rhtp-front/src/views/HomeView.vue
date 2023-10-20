<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="hero min-h-screen bg-base-200">
    <div class="hero-content text-center">
      <div class="max-w-md">
        <h1 class="text-5xl font-bold">Rapid Healthcare Telemedicine Platform</h1>
        <p class="py-6">Want to Build a Telemedicine Platform for Online Doctor Consultation?</p>
        <div class="flex flex-row gap-3 justify-center">
          <RouterLink class="btn btn-primary" to="/register">Get Started</RouterLink>
          <RouterLink class="btn btn-primary" to="/login">Login</RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>
