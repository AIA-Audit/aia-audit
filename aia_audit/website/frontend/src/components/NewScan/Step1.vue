<script setup>
const scanType = [
  {
    name: 'Reconnaissance Scan',
    description: 'Check for the existence of a target and its accessibility. This scan is not intrusive and does not perform any attack.',
    status: 'Enabled',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M9.348 14.651a3.75 3.75 0 010-5.303m5.304 0a3.75 3.75 0 010 5.303m-7.425 2.122a6.75 6.75 0 010-9.546m9.546 0a6.75 6.75 0 010 9.546M5.106 18.894c-3.808-3.808-3.808-9.98 0-13.789m13.788 0c3.808 3.808 3.808 9.981 0 13.79M12 12h.008v.007H12V12zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" /></svg>'
  },
  {
    name: 'Modular Scan',
    description: 'Custom scan allows you to select the modules you want to run.',
    status: 'Enabled',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M21 7.5l-9-5.25L3 7.5m18 0l-9 5.25m9-5.25v9l-9 5.25M3 7.5l9 5.25M3 7.5v9l9 5.25m0-9v9" /></svg>'
  },
]
</script>

<template>
    <div>
        <ul role="list" class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
            <li v-for="(sType,index) in scanType" @click="$emit('setScanType', index+1)" class="col-span-1 divide-y divide-gray-200 rounded-lg bg-white shadow" :class="sType.status === 'Disabled' ? 'hover:bg-gray-200  cursor-not-allowed' : 'hover:bg-green-50 cursor-pointer'">
                <div class="flex w-full items-center justify-between space-x-6 p-6">
                    <div class="flex-1">
                        <div class="flex items-center space-x-3">
                            <h3 class="truncate text-sm font-medium text-gray-900">{{ sType.name }}</h3>
                            <span class="inline-block flex-shrink-0 rounded-full px-2 py-0.5 text-xs font-medium" :class="sType.status === 'Disabled' ? ['text-white', 'bg-red-500'] : ['text-white', 'bg-green-500']">{{ sType.status }}</span>
                        </div>
                        <p class="mt-1 text-sm text-gray-500">{{ sType.description }}</p>
                    </div>
                    <span v-html="sType.icon"></span>
                </div>
            </li>
        </ul>
    </div>
</template>