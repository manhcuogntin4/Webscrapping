<template>
    <v-app>
         <v-navigation-drawer
      v-model="sideNav" temporary absolute>
    <v-list>
    <v-list-item>

    <v-list-item-action>
        <v-icon>account_balance</v-icon>
    </v-list-item-action>
        <v-list-item-content>compare gold price</v-list-item-content>
    </v-list-item>
        <v-list-item>

    <v-list-item-action>
         <v-icon>room</v-icon>
    </v-list-item-action>
             <v-list-item-content>find a gold shop</v-list-item-content>
    </v-list-item>
        <v-list-item>
    <v-list-item-action>
         <v-icon>search</v-icon>
    </v-list-item-action>
             <v-list-item-content>search</v-list-item-content>
    </v-list-item>
    </v-list>
    </v-navigation-drawer>

     <v-toolbar dark class="purple darken-1" style="height:3px;">
         <v-app-bar-nav-icon @click.stop="sideNav=!sideNav" class="hidden-sm-and-up"></v-app-bar-nav-icon>
     <v-toolbar-title>Gold digger</v-toolbar-title>

    <v-spacer></v-spacer>
    <v-toolbar-items class="hidden-xs-only" style="height:3px;">
      <v-btn icon color="red">
          <v-icon>account_balance</v-icon>
      </v-btn>
      <v-btn icon color="red">
          <v-icon>room</v-icon>
      </v-btn>
      <v-btn icon color="red">
            <v-icon>
              search
          </v-icon>
          </v-btn>
    </v-toolbar-items>
  </v-toolbar>
     <main>
        <v-content>
            <search></search>
            <gold name="100"/>
            <gold name="200"/>

        </v-content>
     </main>

    </v-app>
</template>

<script>

    import gold from './components/gold';
    import Search from "./components/search";


    export default {
        name: 'App',
        components: {
            Search,
            gold,

        },
        data: () => ({

              sideNav:false
        }),
    };
</script>
