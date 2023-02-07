<template>
    <div class="grid grid-cols-2 px-4 py-4 shadow-md rounded-md">
        <!-- Target Settings-->
        <div>
            <label class="block text-md font-medium text-blue-500 mb-4">
                Target
            </label>
            <div class="mb-4">
                <label class="block text-sm font-medium text-gray-800 mb-2">
                    Target Type
                </label>
                <div class="flex items-center mb-1">
                    <input v-model="targetType" id="target-type-1" name="target-type" type="radio" value=1 class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300">
                    <label for="target-type-1" class="ml-2 text-sm font-medium text-gray-700 dark:text-gray-500">Host</label>
                </div>
                <div class="flex items-center">
                    <input v-model="targetType" id="target-type-2" name="target-type" type="radio" value=2 class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300">
                    <label for="target-type-2" class="ml-2 text-sm font-medium text-gray-700 dark:text-gray-500">Network</label>
                </div>
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-800 mb-2">
                    <template v-if="targetType == 1">
                        Enter your target host:
                    </template>
                    <template v-if="targetType == 2">
                        Enter your target network:
                    </template>
                </label>
                <input v-model="target" type="text" id="target" class="w-3/4 border border-gray-300 text-gray-700 text-sm rounded-lg focus:outline-none focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" :placeholder="targetPlaceholder" required>
            </div>
        </div>
        <!-- Modules Settings -->
        <div>
            <label class="block text-md font-medium text-blue-500 mb-4 w-3/4">
                Modules
            </label>
            <div class="mb-4">
                <!-- Modules PickList-->
                <PickList v-model="modules" dataKey="id" :showSourceControls="false" :showTargetControls="false">
                    <template #sourceheader>
                        Available
                    </template>
                    <template #targetheader>
                        Selected
                    </template>
                    <template #item="slotProps">
                        {{ slotProps.item.name }}
                    </template>
                </PickList>
            </div>
        </div>
    </div>
</template>

<script>
import PickList from 'primevue/picklist';

export default {
    components: {
        PickList
    },
    data() {
        return {
        }
    },
    props: {
        target: String,
        targetType: Number,
        modules: Array
    },
    computed: {
        targetPlaceholder() {
            if(this.targetType == 1) return 'Example: 192.168.203.100';
            else return 'Example: 192.168.203.0/24';
        }
    },
}
</script>

<style>
.p-picklist .p-button{
    border: 1px solid #3b82f6!important; 
    background-color: #3b82f6!important;
}

.p-picklist .p-picklist-list .p-picklist-item.p-highlight{
    color: #3b82f6!important;
}

.p-picklist-header{
    font-size: 12px!important;
}
</style>