<template>
    <v-slide-y-transition
            mode="in-out"
            class="row py-2"
            group
            tag="div"
    >
        <v-col cols="12" v-for="gold in golds" :key="gold.name">
            <gold :gold="gold" @delete="deletegold(gold)"
                     @update="updategold(gold)"/>
        </v-col>
    </v-slide-y-transition>
</template>

<script>
    import axios from 'axios';
    import gold from './gold.vue';

    export default {
        name: "goldlist",
        props: ['search'],
        data: () => ({
            golds: []
        }),
        components: {
            gold,
        },
        watch: {
            search() {
                this.searchGolds();
            }
        },
        created() {
            this.searchGolds();
        },
        methods: {
            searchGolds() {
                let search = this.search;
                if (!search) {
                    search = "";
                }

                let params = {query: search};
                axios.get('http://localhost:8000/api/v1/golds', {params: params}).then((response) => {
                    this.golds = response.data;
                });
            },
            updateGold(gold) {
                axios.get('http://localhost:8000/api/v1/gold/' + gold.name).then((response) => {
                    let index_of_gold = this.golds.indexOf(gold);
                    let new_gold = response.data;
                    this.golds.splice(index_of_gold, 1, new_gold);
                });
            },
            deleteGold(gold) {
                let index_of_gold = this.golds.indexOf(gold);
                this.golds.splice(index_of_gold, 1);
            }
        }
    }
</script>


