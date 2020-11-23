<template>
  <v-main>
    <div class="Login">
      <LoginComponent />
    </div>
  </v-main>
</template>

<script>
import LoginComponent from "@/components/LoginComponent.vue";

export default {
  name: "Login",
  components: {
    LoginComponent,
  },
};
</script>
