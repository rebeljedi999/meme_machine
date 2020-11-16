<template>
  <div>
    <Editor :canvasWidth="canvasWidth" :canvasHeight="canvasHeight" ref="editor"/>
    <input id="chooseImage" type="file" @change="uploadImage($event)" accept="image/*"/>
    <v-btn v-on:click="textMode()">Text Mode</v-btn>
    <v-btn v-on:click="download()">Download</v-btn>

  </div>
</template>

<script>
import Editor from "vue-image-markup";

export default {
  name: 'App',

  components: {
    Editor
  },

  data() {
    return {
      color: "black",
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
      this.$refs.editor.set('text');
    },
    download() {
      let link = document.createElement("a");
      link.setAttribute("href", this.$refs.editor.saveImage());
      link.setAttribute("download", "image-markup");
      link.click();
    }
  },
};

</script>
