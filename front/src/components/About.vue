<template>
    <v-app>
        <Banner></Banner>
        <v-content>

                <v-card class="mx-auto" max-width="500">
            <v-img
              src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
              height="200px"
            ></v-img>

            <v-card-title>
              Comparator for the price of the gold
            </v-card-title>

            <v-card-subtitle>
              Expert in the domain
            </v-card-subtitle>

            <v-card-actions>
              <v-btn text>Share</v-btn>
             <v-btn
        color="purple"
        text
      >
        Explore
      </v-btn>

      <v-spacer></v-spacer>

      <v-btn
        icon
        @click="show = !show"
      >
        <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
      </v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text>
          I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
        </v-content>
    </v-app>
</template>

<script>

    import Banner from './Banner.vue';


    export default {
        name: 'home',
        components: {
         Banner
        },
        data() {
            return {

            }
        },
        methods: {
            setAuthenticated(status) {
                this.authenticated = status;
            },
            logout() {
                this.authenticated = false;
            }
        }
    };
</script>