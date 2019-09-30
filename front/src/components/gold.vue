<template>
    <v-container>
        <v-layout v-if="gold !== null">
            <v-flex xs12>
                <v-card class="mx-auto">
                    <v-list-item three-line>
                        <v-list-item-content>
                            <div class="overline mb-4">OVERLINE</div>
                            <v-list-item-title class="headline mb-1">{{ gold.name }}</v-list-item-title>
                            <v-list-item-subtitle>{{ gold.url }}</v-list-item-subtitle>
                            <v-list-item-subtitle>{{ gold.prix }}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    import axios from 'axios';

    export default {
        props: ['name'],
        data: () => ({
            gold: null
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