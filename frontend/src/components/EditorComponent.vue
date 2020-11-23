<template>
  <div class="EditorComponent">
    <v-container>
      <v-row>
        <v-col cols="12" sm="2">
          <v-sheet rounded="lg" min-height="268">
            <v-color-picker
              dot-size="25"
              swatches-max-height="200"
              hide-canvas
              hide-inputs
              show-swatches
              value="99999"
              @update:color="Color"
            ></v-color-picker>
          </v-sheet>
        </v-col>
        <v-col cols="12" sm="8">
          <v-sheet min-height="70vh" rounded="lg">
            <Editor
              :canvasWidth="canvasWidth"
              :canvasHeight="canvasHeight"
              ref="editor"
            />
          </v-sheet>
        </v-col>
        <v-col cols="12" sm="2">
          <v-sheet rounded="lg" min-height="268">
            <input
              id="chooseImage"
              type="file"
              @change="uploadImage($event)"
              accept="image/*"
            />
            <v-container>
              <v-btn v-on:click="textMode()">Text Mode</v-btn>
              <v-btn v-on:click="download()">Download Image</v-btn>
              <v-btn v-on:click="save()">Save</v-btn>
            </v-container>
            <v-container>
              <v-card
                v-on:click="uploadImage('@/assets/Template1.jpg')"
                type="file"
              >
                <v-img
                  src="@/assets/Template1.jpg"
                  max-height="250"
                  max-width="250"
                ></v-img>
              </v-card>
              <v-card v-on:click="setImage(`@/assets/Template1.jpg`)">
                <v-img
                  src="@/assets/Template1.jpg"
                  max-height="250"
                  max-width="250"
                ></v-img>
              </v-card>
            </v-container>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import Editor from "vue-image-markup";
import axios from 'axios';
require("@/assets/Template1.jpg");

export default {
  name: "EditorComponent",

  components: {
    Editor,
  },

  data() {
    return {
      color: "",
      imageUrl: "@/assets/Template1.jpg",
      uid: localStorage.getItem("user-token"),
    };
  },
  props: {
    canvasWidth: {
      default: 600,
    },
    canvasHeight: {
      default: 600,
    },
  },
  mounted() {
    if (this.imageUrl) {
      this.$refs.editor.setBackgroundImage(this.imageUrl);
    }
  },
  methods: {
    uploadImage(e) {
      this.$refs.editor.uploadImage(e);
    },
    textMode() {
      this.$refs.editor.set("text");
    },
    download() {
      let link = document.createElement("a");
      link.setAttribute("href", this.$refs.editor.saveImage());
      link.setAttribute("download", "Image");
      link.click();
    },
    Color(e) {
      this.color = e.hex;
      this.$refs.editor.changeColor(this.color);
    },
    Undochange() {
      this.$refs.editor.undo();
    },
    save() {
      const base64 = this.$refs.editor.saveImage();
      run().catch((err) => console.log(err));
      async function run() {
        const blob = await fetch(base64).then((res) => res.blob());
        const formData = new FormData();
        formData.append("file", blob);
        formData.append("title", "Image");
        const res = await axios.post("//localhost:8000/memes/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
            "Authorization": "Token ".concat(String(localStorage.getItem("user-token"))),
          },
        });
        console.log(res.data);
      }
    },
  },
};
</script>

<style scoped>
</style>