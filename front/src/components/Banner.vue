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
          <v-btn text @click='go_About()'>ABOUT</v-btn>
      </v-toolbar-items>
      </div>
      <div class="flex-grow-1"></div>
      <v-text-field :label="search" v-model="search_text"
                                                single-line>Search</v-text-field>
      <v-btn icon @click="search()">
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
          <v-list-item @click="login()" target="_blank">
            <v-list-item-title>Login</v-list-item-title>
          </v-list-item>
          <v-list-item @click="logout()" target="_blank">
            <v-list-item-title>Logout</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
  </div>
</template>
<script>
import {Authentique} from '../main.js';
import  { EventBus } from '../event-bus.js';
export default {
  name: 'Banner',
        data:() => ({
        search_text:'',
        }),
    methods: {
            go_Home() {
                this.$router.replace('/home');

            },
            go_About(){
                 this.$router.replace('/about');
            },
             go_Add(){
                 this.$router.replace('/add');
            },
            login(){
                this.$router.replace('/login');
            },
            logout(){
                Authentique.is_authentique=false;
                this.$router.go(this.$router.currentRoute)
            },
            search(){
                console.log("Banner",this.search_text);
                Authentique.search=this.search_text;
                this.$emit('update',{item:this.search_text});
                EventBus.$emit('update_banner', this.search_text);
                console.log("Emit",this.search_text);
            }
        }
}
</script>
