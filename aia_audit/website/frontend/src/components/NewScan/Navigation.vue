<script setup>
import { defineProps, reactive } from "vue";
const props = defineProps({
    scanType: Number,
    currentStep: Number,
});
</script>

<template>
    <template v-if="currentStep > 1">
    <div class="flex justify-between text-lg mb-4 p-2 rounded-md">
        <h3 class="font-bold text-gray-700">
             <template v-if="scanType == 1">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="inline-block w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M9.348 14.651a3.75 3.75 0 010-5.303m5.304 0a3.75 3.75 0 010 5.303m-7.425 2.122a6.75 6.75 0 010-9.546m9.546 0a6.75 6.75 0 010 9.546M5.106 18.894c-3.808-3.808-3.808-9.98 0-13.789m13.788 0c3.808 3.808 3.808 9.981 0 13.79M12 12h.008v.007H12V12zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" /></svg>
                Reconnaissance Scan
            </template>
            <template v-else-if="scanType == 2">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="inline-block w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M21 7.5l-9-5.25L3 7.5m18 0l-9 5.25m9-5.25v9l-9 5.25M3 7.5l9 5.25M3 7.5v9l9 5.25m0-9v9" /></svg>
                Modular Scan
            </template>
        </h3>
        <div class="flex">
            <button @click="$emit('prevStep')" class="mx-2 text-white bg-blue-500 hover:text-white hover:bg-blue-600 group flex items-center px-2 py-2 text-sm leading-6 font-medium rounded-md">
                Prev Step
            </button>
            <template v-if="currentStep < 3">
            <button @click="$emit('nextStep')" class="mx-2 text-white bg-blue-500 hover:text-white hover:bg-blue-600 group flex items-center px-2 py-2 text-sm leading-6 font-medium rounded-md">
                Next Step
            </button>
            </template>
            <template v-if="currentStep == 3">
            <button @click="$emit('startScan')" class="mx-2 text-white bg-green-500 hover:text-white hover:bg-blue-600 group flex items-center px-2 py-2 text-sm leading-6 font-medium rounded-md">
                Run Scan
            </button>
            </template>
        </div>
    </div>
    </template>
</template>