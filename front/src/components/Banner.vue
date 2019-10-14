<template>
  <div>
    <v-app-bar
      color="deep-purple accent-4"
      dark
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Gold Comparater</v-toolbar-title>
      <div>
      <v-toolbar-items>
          <v-btn text>LINK 1</v-btn>
          <v-btn text>LINK 2</v-btn>
          <v-btn text>LINK 3</v-btn>
          <v-btn text>LINK 4</v-btn>
      </v-toolbar-items>
      </div>
      <div class="flex-grow-1"></div>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-menu
        left
        bottom
      >
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item href="/login" target="_blank">
            <v-list-item-title>Login</v-list-item-title>
          </v-list-item>
          <v-list-item href="http://google.com" target="_blank">
            <v-list-item-title>Logout</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
  </div>
</template>
<script>
export default {
  name: 'Banner',

}
</script>
