<template>
  <div>
    <v-card class="form">
      <v-card-text>
        <v-card-title class="justify-left">
          Meme Machine
        </v-card-title>
        <v-form ref="loginForm" @submit.prevent="login" v-if="token == null">
          <v-row>
            <v-col cols="12">
              <v-text-field
                v-model="loginUser"
                label="Login Name"
                required
              ></v-text-field>
            </v-col>
            <v-col>
              <v-text-field
                v-model="loginPass"
                :type="showpass ? 'text' : 'password'"
                label="Password"
                counter
                @click:append="showpass = !showpass"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-btn size="large" type="submit" color="grey">
            Login
          </v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LoginForm",
  data: () => ({
    showpass: false,
    username: "",
    password: "",
    token: null,
  }),
  methods: {
    login() {
      axios
        .post("http://127.0.0.1:8000/auth/", {
          username: this.loginUser,
          password: this.loginPass,
        })
        .then((resp) => {
          this.token = resp.data.token;
          localStorage.setItem("user-token", resp.data.token);
          localStorage.setItem("user-id", resp.data.id);
          this.$router.push('/');
        })
        .catch((err) => {
          localStorage.removeItem("user-token");
          console.log(err);
        });
    },
  },
};
</script>

<style scoped>
</style>
