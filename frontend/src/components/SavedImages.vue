<template>
  <div>
    <v-row>
      <v-col cols="5" v-for="index in imagelist" :key="index.id">
        <v-card
          v-on:click="
            download(`http://localhost:8000/download`.concat(index.image))
          "
        >
          <v-img
            :src="`http://localhost:8000/download`.concat(index.image)"
            class="image"
          ></v-img>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SavedImages",
  data: () => ({
    imagelist: [],
  }),
  methods: {
    imageretrieval() {
      axios
        .get(
          `http://127.0.0.1:8000/memes/?user=${localStorage.getItem(
            "user-id"
          )}`,
          {
            headers: {
              "Content-Type": "multipart/form-data",
              Authorization: "Token ".concat(
                String(localStorage.getItem("user-token"))
              ),
            },
          }
        )
        .then((response) => {
          this.imagelist = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    download(url) {
      axios
        .get(url, {responseType: "arraybuffer"})
        .then((response) => {
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement("a");
          link.href = url;
          link.setAttribute("download", "Meme.png");
          document.body.appendChild(link);
          link.click();
        })
        .catch((err) => console.log(err));
    },
  },
  beforeMount() {
    this.imageretrieval();
  },
};
</script>

<style scoped>
</style>