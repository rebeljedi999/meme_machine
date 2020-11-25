<template>
  <v-main>
    <div class="SavedImages">
      <SavedImages />
    </div>
  </v-main>
</template>

<script>
import SavedImages from "@/components/SavedImages.vue";

export default {
  name: "Saved",
  components: {
    SavedImages,
  },
};
</script>
