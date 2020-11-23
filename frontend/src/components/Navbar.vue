<template>
  <nav>
    <div>
      <v-toolbar>
      <v-toolbar-title class="text-uppercase white--text">
        <v-btn color="grey" class="btn" medium to="/">
          <span>Meme Machine</span>
        </v-btn>
      </v-toolbar-title>
      <v-btn color="grey" class="btn" small>
        <span>Button 1</span>
      </v-btn>
      <v-btn color="grey" class="btn" small>
        <span>Button 2</span>
      </v-btn>
      <v-btn color="grey" class="btn" small>
        <span>Button 3</span>
      </v-btn>
      </v-toolbar>
    </div>
  </nav>
</template>

<script>
export default {};
</script>

<style scoped>
.btn {
  margin-left: 20px;
}

.link {
  text-decoration: none;
  color: "inherit";
}
</style>
