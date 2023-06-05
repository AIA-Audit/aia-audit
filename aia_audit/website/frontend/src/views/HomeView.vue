<template>
    <div class="mt-8">
        <Stats />
        <div class="my-4">
            <h2 class="text-2xl font-bold text-gray-700 mt-4 mb-2">Last scans</h2>
            <DataTable :value="scans">
                <Column field="id" header="Code"></Column>
                <Column field="name" header="Name"></Column>
                <Column header="Started at">
                    <template #body="slotProps">
                        {{ unixToTimestamp(slotProps.data.start_time) }}
                    </template>
                </Column>
                <Column header="End at">
                    <template #body="slotProps">
                        {{ unixToTimestamp(slotProps.data.end_time) }}
                    </template>
                </Column>
                <Column field="target" header="target"></Column>
                <Column header="">
                    <template #body="slotProps">
                        <div class="flex justify-center">
                            <router-link :to="{ name: 'scan', params: { id: slotProps.data.id } }"
                                class="text-center text-white bg-blue-500 hover:bg-blue-600 px-4 py-2 rounded-md">View
                                results</router-link>
                        </div>
                    </template>
                </Column>
                <template #empty> No scans performed yet </template>
            </DataTable>
        </div>
    </div>
</template>

<script setup>
import Button from 'primevue/button';
import Dialog from 'primevue/dialog';
</script>

<script>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';   // optional
import Row from 'primevue/row';                   // optional
import Stats from "@/components/Home/Stats.vue";

export default {
    name: 'Home',
    components: {
        Stats,
        DataTable,
        Column,
        ColumnGroup,
        Row
    },
    data() {
        return {
            scans: []
        }
    },
    mounted(){
        this.axios.get('/api/data/scans/last/5').then((response) => {
            console.log(response.data);
            this.scans = response.data;
        });
    },
    methods: {
        unixToTimestamp(unixdate) {
            console.log(unixdate);
            return this.moment.unix(unixdate).format('DD/MM/YYYY HH:mm:ss');
        }
    }
}
</script>