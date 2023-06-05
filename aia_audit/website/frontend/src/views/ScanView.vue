<template>
    <div class="grid grid-cols-6 gap-4">
        <div class="col col-span-4 px-2 py-4">
            <div class="shadow-md rounded">
                <!-- Header -->
                <div class="bg-blue-500 text-white px-4 py-2">
                    <h2 class="text-xl font-bold">Scan modules</h2>
                </div>
                <!-- Content -->
                <div>
                    <DataTable v-model:expandedRows="expandedRows" :value="scan_data.results" datakey="id"
                        tableStyle="width: 100%">
                        <Column expander style="width: 5rem" />
                        <Column field="name" header="Module name" />
                        <Column header="Stats">
                            <template #body="slotProps">
                                <template v-if="countModuleVulnerabilitiesBySeverity(slotProps, 'info') > 0">
                                    <span class="text-xs font-bold px-4 py-2 text-white rounded-md bg-blue-500 mr-2">
                                        {{ countModuleVulnerabilitiesBySeverity(slotProps, "info") }}
                                    </span>
                                </template>
                                <template v-if="countModuleVulnerabilitiesBySeverity(slotProps, 'low') > 0">
                                    <span class="text-xs font-bold px-4 py-2 text-white rounded-md bg-green-500 mr-2">
                                        {{ countModuleVulnerabilitiesBySeverity(slotProps, "low") }}
                                    </span>
                                </template>
                                <template v-if="countModuleVulnerabilitiesBySeverity(slotProps, 'medium') > 0">
                                    <span class="text-xs font-bold px-4 py-2 text-white rounded-md bg-yellow-500 mr-2">
                                        {{ countModuleVulnerabilitiesBySeverity(slotProps, "medium") }}
                                    </span>
                                </template>
                                <template v-if="countModuleVulnerabilitiesBySeverity(slotProps, 'high') > 0">
                                    <span class="text-xs font-bold px-4 py-2 text-white rounded-md bg-orange-500 mr-2">
                                        {{ countModuleVulnerabilitiesBySeverity(slotProps, "high") }}
                                    </span>
                                </template>
                                <template v-if="countModuleVulnerabilitiesBySeverity(slotProps, 'critical') > 0">
                                    <span class="text-xs font-bold px-4 py-2 text-white rounded-md bg-red-500">
                                        {{ countModuleVulnerabilitiesBySeverity(slotProps, "critical") }}
                                    </span>
                                </template>
                            </template>
                        </Column>
                        <template #expansion="slotProps">
                            <DataTable v-model:expandedRows="expandedDevicesRows" datakey="id"
                                :value="scan_data.results[slotProps.index].devices" tableStyle="width: 100%">
                                <Column expander style="width: 5rem" />
                                <Column field="ip" header="IP Address / Network Address" />
                                <template #expansion="slotProps2">
                                    <DataTable v-model:expandedRows="expandedDevicesVulnerabilitiesRows" datakey="id"
                                        :value="slotProps2.data.vulnerabilities" tableStyle="width: 100%">
                                        <Column expander style="width: 5rem" />
                                        <Column field="name" header="Vulnerability name" />
                                        <Column field="description" header="Vulnerability description" />
                                        <Column header="Severity">
                                            <template #body="slotProps3">
                                                <span class="text-sm font-bold px-4 py-2 text-white rounded-md"
                                                    :class="slotProps3.data.severity == 'critical' ? 'bg-red-500' : slotProps3.data.severity == 'high' ? 'bg-orange-500' : slotProps3.data.severity == 'medium' ? 'bg-yellow-500' : slotProps3.data.severity == 'low' ? 'bg-green-500' : 'bg-blue-500'">
                                                    {{ slotProps3.data.severity }}
                                                </span>
                                            </template>
                                        </Column>
                                        <template #expansion="slotProps4">
                                            <div class="px-2 py-4 text-gray-700 w-full text-xs overflow-scroll">
                                                <pre>{{ slotProps4.data.output }}</pre>
                                            </div>
                                        </template>
                                    </DataTable>
                                </template>
                            </DataTable>
                        </template>
                    </DataTable>
                </div>
            </div>
        </div>
        <div class="col col-span-2 px-4 py-4">
            <div class="shadow-md rounded">
                <!-- Header -->
                <div class="bg-blue-500 text-white px-4 py-2">
                    <h2 class="text-xl font-bold">Scan status</h2>
                </div>
                <!-- Content -->
                <div class="px-2 py-4 text-gray-700">
                    Scan ID: {{ scan_data.id }}<br>
                    Scan name: {{ scan_data.name }}<br>
                    Scan target: {{ scan_data.target }}<br>
                    Scan start time: {{ unixToTimestamp(scan_data.start_time) }}<br>
                    Scan end time: {{ unixToTimestamp(scan_data.end_time) }}
                </div>
            </div>
            <div class="shadow-md rounded mt-8">
                <!-- Header -->
                <div class="bg-blue-500 text-white px-4 py-2">
                    <h2 class="text-xl font-bold">Vulnerabilities</h2>
                </div>
                <!-- Content -->
                <div class="px-2 py-4 text-gray-700">
                    <Chart type="doughnut" :data="chartData" :options="chartOptions" class="mx-auto" style="width: 75%;" />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Chart from 'primevue/chart';
import { computed } from 'vue';

export default {
    components: {
        DataTable,
        Chart,
        Column
    },
    data() {
        return {
            expandedRows: [],
            expandedDevicesRows: [],
            expandedDevicesVulnerabilitiesRows: [],
            scan_data: {},
            chartData: null,
            chartOptions: {
                cutout: '50%'
            }
        }
    },
    methods: {
        setChartData() {
            const documentStyle = getComputedStyle(document.body);
            return {
                labels: ['Critical', 'High', 'Medium', 'Low', 'Info'],
                datasets: [
                    {
                        data: [this.countAllModulesVulnerabilitiesBySeverity('critical'), this.countAllModulesVulnerabilitiesBySeverity('high'), this.countAllModulesVulnerabilitiesBySeverity('medium'), this.countAllModulesVulnerabilitiesBySeverity('low'), this.countAllModulesVulnerabilitiesBySeverity('info')],
                        backgroundColor: [documentStyle.getPropertyValue('--red-500'), documentStyle.getPropertyValue('--orange-500'), documentStyle.getPropertyValue('--yellow-500'), documentStyle.getPropertyValue('--green-500'), documentStyle.getPropertyValue('--blue-500')],
                    }
                ]
            };
        },
        countAllModulesVulnerabilitiesBySeverity(severity){
            let count = 0;
            for (var i = 0; i < this.scan_data.results.length; i++) {
                for (var j = 0; j < this.scan_data.results[i].devices.length; j++) {
                    for (var k = 0; k < this.scan_data.results[i].devices[j].vulnerabilities.length; k++) {
                        if (this.scan_data.results[i].devices[j].vulnerabilities[k].severity == severity) {
                            count++;
                        }
                    }
                }
            }
            return count;
        },
        countModuleVulnerabilitiesBySeverity(data, severity) {
            let count = 0;
            for (var i = 0; i < data.data.devices.length; i++) {
                for (var j = 0; j < data.data.devices[i].vulnerabilities.length; j++) {
                    if (data.data.devices[i].vulnerabilities[j].severity == severity) {
                        count++;
                    }
                }
            }
            return count;
        },
        unixToTimestamp(unixdate) {
            return this.moment.unix(unixdate).format('DD/MM/YYYY HH:mm:ss');
        }
    },
    mounted() {
        this.axios.get('/api/data/scan/' + this.$route.params.id).then(response => {
            this.scan_data = response.data[0];
            this.scan_data.results = JSON.parse(this.scan_data.results);
            for (let i = 0; i < this.scan_data.results.length; i++) {
                this.scan_data.results[i].id = Math.floor(Math.random() * 100000);
                for (let j = 0; j < this.scan_data.results[i].devices.length; j++) {
                    this.scan_data.results[i].devices[j].id = Math.floor(Math.random() * 100000);
                    for (let k = 0; k < this.scan_data.results[i].devices[j].vulnerabilities.length; k++) {
                        this.scan_data.results[i].devices[j].vulnerabilities[k].id = Math.floor(Math.random() * 100000);
                    }
                }
            }
            this.chartData = this.setChartData();
        });
    },
}
</script>