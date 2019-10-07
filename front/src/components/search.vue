<template>
    <v-card>
<v-form>
    <v-container>
      <v-row>

        <v-col cols="12" sm="4">

          <v-select
                  outlined
            prepend-inner-icon="menu"

          ></v-select>

        </v-col>

        <v-col cols="12" sm="4">

          <v-text-field outlined
                        placeholder="search ..."
            append-icon="search"

          ></v-text-field>

        </v-col>
        <v-col cols="12" sm="4">
          <v-text-field

            outlined
            placeholder="city"
            append-icon="place"
          ></v-text-field>

        </v-col>

      </v-row>
    </v-container>
  </v-form>
        </v-card>
</template>


<script>
    import axios from 'axios';

    export default {
        props: ['name'],
        data: () => ({
            //
        }),
        created() {
            console.log('created called.');
            axios.get('http://localhost:8000/api/v1/gold/' + this.name).then((response) => {
                this.gold = response.data;
                alert("Hello World")
            });
        }
    };
</script>
