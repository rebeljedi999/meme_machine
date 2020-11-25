<template>
  <div class="EditorComponent">
    <v-container>
      <v-row>
        <v-col cols="12" sm="2">
          <v-container fluid>
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
          </v-container>
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
            <v-container fluid>
              <input
                id="chooseImage"
                type="file"
                @change="uploadImage($event)"
                style="color: grey"
                accept="image/*"
              />
              <v-btn v-on:click="textMode()" block>Text Mode</v-btn>
              <v-btn v-on:click="$refs.editor.set('freeDrawing')" block
                >Draw Mode</v-btn
              >
              <v-btn v-on:click="download()" block>Download</v-btn>
              <v-btn v-on:click="save()" block>Save</v-btn>
              <v-btn v-on:click="$refs.editor.undo()" block>Undo</v-btn>
              <v-btn v-on:click="$refs.editor.redo()" block>Redo</v-btn>
            </v-container>
            <v-container>
              <v-card v-on:click="downloadTemplate(a)">
                <v-img
                  :src="this.memes.data.memes[this.a].url"
                  max-height="300"
                  max-width="300"
                ></v-img>
              </v-card>
              <v-card v-on:click="downloadTemplate(b)">
                <v-img
                  :src="this.memes.data.memes[this.b].url"
                  max-height="300"
                  max-width="300"
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
import axios from "axios";
require("@/assets/Template1.jpg");

export default {
  name: "EditorComponent",

  components: {
    Editor,
  },

  data() {
    return {
      color: "",
      imageUrl: null,
      uid: localStorage.getItem("user-token"),
      memes: [],
      a: Math.floor(Math.random() * 100),
      b: Math.floor(Math.random() * 100),
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
    axios
    .get('https://api.imgflip.com/get_memes')
    .then((response) => {
      this.memes = response.data
    })
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
            Authorization: "Token ".concat(
              String(localStorage.getItem("user-token"))
            ),
          },
        });
        console.log(res.data);
      }
    },
    downloadTemplate(val) {
      axios
        .get(this.memes.data.memes[val].url, { responseType: "arraybuffer" })
        .then((response) => {
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement("a");
          link.href = url;
          link.setAttribute("download", "Template.png");
          document.body.appendChild(link);
          link.click();
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style scoped>
input[type="file"] {
  color: transparent;
}
</style>
