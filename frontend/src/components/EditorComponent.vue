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
            <v-btn v-on:click="textMode()">Text Mode</v-btn>
            <v-btn v-on:click="download()">Download Image</v-btn>
            <v-btn v-on:click="this.$refs.editor.redo()">Redo</v-btn>
            <v-btn v-on:click="this.$refs.editor.undo()"> Undo</v-btn>
            <v-btn v-on:click="this.$refs.editor.clear()">Clear</v-btn>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
    </div>
</template>

<script>

import Editor from "vue-image-markup";

export default {
  name: "EditorComponent",

  components: {
    Editor,
  },

  data() {
    return {
      color: "",
      imageUrl: null,
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
      link.setAttribute("download", "image-markup");
      link.click();
    },
    Color(e) {
      this.color = e.hex
      this.$refs.editor.changeColor(this.color);
    },
  },
};
</script>

<style scoped>
</style>