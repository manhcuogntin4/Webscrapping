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
          <v-btn text @click='go_Home()'>HOME</v-btn>
          <v-btn text @click='go_Add()'>ADD</v-btn>
          <v-btn text>EXPERT</v-btn>
          <v-btn text @click='go_About()'>ABOUT</v-btn>
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
methods: {
            go_Home() {
                this.$router.replace('/home');

            },
            go_About(){
                 this.$router.replace('/about');
            },
             go_Add(){
                 this.$router.replace('/add');
            }
        }
}
</script>
