<template>
  <v-main>
    <div class="EditorComponent">
      <EditorComponent />
    </div>
  </v-main>
</template>

<script>
import EditorComponent from "@/components/EditorComponent.vue";

export default {
  name: "Home",
  components: {
    EditorComponent,
  },
};
</script>
