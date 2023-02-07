<script setup>
import { defineProps, reactive } from "vue";
const props = defineProps({
  currentStep: Number,
});

const steps = [
  { id: 'Step 1', name: 'Select Scan Type', href: '#', status: 'current' },
  { id: 'Step 2', name: 'Configure the scan', href: '#', status: 'upcoming' },
  { id: 'Step 3', name: 'Perform the scan', href: '#', status: 'upcoming' },
]
</script>

<template>
<!-- Steps Section -->
<div class="mb-8">
  <nav aria-label="Progress">
    <ol role="list" class="space-y-4 md:flex md:space-y-0 md:space-x-8">
      <li v-for="(step, index) in steps" :key="step.name" class="md:flex-1">
        <a v-if="index+1 < currentStep" :href="step.href" class="group flex flex-col border-l-4 border-gray-700 py-2 pl-4 hover:border-blue-700 md:border-l-0 md:border-t-4 md:pl-0 md:pt-4 md:pb-0">
          <span class="text-sm font-medium text-blue-600 group-hover:text-blue-700">{{ step.id }}</span>
          <span class="text-sm font-medium text-gray-700">{{ step.name }}</span>
        </a>
        <a v-else-if="index+1 === currentStep" :href="step.href" class="flex flex-col border-l-4 border-blue-500 py-2 pl-4 md:border-l-0 md:border-t-4 md:pl-0 md:pt-4 md:pb-0" aria-current="step">
          <span class="text-sm font-medium text-blue-600">{{ step.id }}</span>
          <span class="text-sm font-medium text-gray-700">{{ step.name }}</span>
        </a>
        <a v-else :href="step.href" class="group flex flex-col border-l-4 border-gray-200 py-2 pl-4 hover:border-gray-300 md:border-l-0 md:border-t-4 md:pl-0 md:pt-4 md:pb-0">
          <span class="text-sm font-medium text-gray-500 group-hover:text-gray-700">{{ step.id }}</span>
          <span class="text-sm font-medium text-gray-700">{{ step.name }}</span>
        </a>
      </li>
    </ol>
  </nav>
</div>
</template>