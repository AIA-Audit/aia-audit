<script setup>
import { RouterLink, RouterView } from "vue-router";
import Button from 'primevue/button';
import Dialog from 'primevue/dialog';
import LogoSVG from "./assets/logo.svg?component";
</script>

<template>
    <!-- Left application (left Modal) -->
    <Dialog header="AIA Audit v0.1" v-model:visible="displayLeftModal" :breakpoints="{'960px': '75vw', '640px': '90vw'}" :style="{width: '50vw'}" :modal="true">
      <p>
          You have left the application successfully. See you soon!
      </p>
    </Dialog>
    <!-- Stop application (exit Modal)-->
    <Dialog header="Do you really want to exit?" v-model:visible="displayExitModal" :breakpoints="{'960px': '75vw', '640px': '90vw'}" :style="{width: '50vw'}" :modal="true">
      <p class="m-0">
          <span class="font-bold">Warning!</span> You are about to exit the application. All unsaved changes will be lost.
      </p>
      <template #footer>
          <Button class="p-button-link" label="No" icon="pi pi-times" @click="displayExitModal = false;"/>
          <Button class="p-button-danger" label="Yes" icon="pi pi-check" @click="stopTool()" autofocus />
      </template>
    </Dialog>
    <!-- End Stop application (exit Modal)-->
    <div class="min-h-full">
        <!-- Static sidebar for desktop -->
        <div class="fixed inset-y-0 flex w-64 flex-col">
            <div class="bg-blue-700 h-full flex flex-col justify-between">
              <div>
                <div class="flex flex-grow flex-col overflow-y-auto pt-5 pb-4">
                    <div class="text-white text-lg font-bold mx-auto">
                        AIA Audit
                    </div>
                    <nav class="mt-5 flex flex-1 flex-col divide-y divide-blue-600 overflow-y-auto" aria-label="Sidebar">
                        <div class="space-y-1 px-2">
                            <router-link :to="{ name: 'home' }" active-class="bg-gray-800" class="text-blue-100 hover:text-white hover:bg-blue-600 group flex items-center px-2 py-2 text-sm leading-6 font-medium rounded-md" aria-current="page">
                              <svg class="mr-4 h-6 w-6 flex-shrink-0 text-blue-200 inline-block" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
                              </svg>                                              
                              Dashboard
                            </router-link>

                            <router-link :to="{ name: 'new-scan' }" active-class="bg-gray-800" class="text-blue-100 hover:text-white hover:bg-blue-600 group flex items-center px-2 py-2 text-sm leading-6 font-medium rounded-md">
                              <svg class="mr-4 h-6 w-6 flex-shrink-0 text-blue-200" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M12 10.5v6m3-3H9m4.06-7.19l-2.12-2.12a1.5 1.5 0 00-1.061-.44H4.5A2.25 2.25 0 002.25 6v12a2.25 2.25 0 002.25 2.25h15A2.25 2.25 0 0021.75 18V9a2.25 2.25 0 00-2.25-2.25h-5.379a1.5 1.5 0 01-1.06-.44z" />
                              </svg>                                                                
                              New Scan
                            </router-link>
        
                            <router-link :to="{ name: 'scans' }" active-class="bg-gray-800" class="text-blue-100 hover:text-white hover:bg-blue-600 group flex items-center px-2 py-2 text-sm leading-6 font-medium rounded-md">
                              <svg class="mr-4 h-6 w-6 flex-shrink-0 text-blue-200" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 15.75l-2.489-2.489m0 0a3.375 3.375 0 10-4.773-4.773 3.375 3.375 0 004.774 4.774zM21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                              </svg>                                    
                              My Scans
                            </router-link>
        
                            <a href="#" class="text-blue-100 hover:text-white hover:bg-blue-600 group flex items-center px-2 py-2 text-sm leading-6 font-medium rounded-md">
                              <svg class="mr-4 h-6 w-6 flex-shrink-0 text-blue-200" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25M9 16.5v.75m3-3v3M15 12v5.25m-4.5-15H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" />
                              </svg> Reports
                            </a>
                          
                            <a href="#" class="text-blue-100 hover:text-white hover:bg-blue-600 group flex items-center px-2 py-2 text-sm leading-6 font-medium rounded-md">
                              <svg class="mr-4 h-6 w-6 flex-shrink-0 text-blue-200" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M14.25 6.087c0-.355.186-.676.401-.959.221-.29.349-.634.349-1.003 0-1.036-1.007-1.875-2.25-1.875s-2.25.84-2.25 1.875c0 .369.128.713.349 1.003.215.283.401.604.401.959v0a.64.64 0 01-.657.643 48.39 48.39 0 01-4.163-.3c.186 1.613.293 3.25.315 4.907a.656.656 0 01-.658.663v0c-.355 0-.676-.186-.959-.401a1.647 1.647 0 00-1.003-.349c-1.036 0-1.875 1.007-1.875 2.25s.84 2.25 1.875 2.25c.369 0 .713-.128 1.003-.349.283-.215.604-.401.959-.401v0c.31 0 .555.26.532.57a48.039 48.039 0 01-.642 5.056c1.518.19 3.058.309 4.616.354a.64.64 0 00.657-.643v0c0-.355-.186-.676-.401-.959a1.647 1.647 0 01-.349-1.003c0-1.035 1.008-1.875 2.25-1.875 1.243 0 2.25.84 2.25 1.875 0 .369-.128.713-.349 1.003-.215.283-.4.604-.4.959v0c0 .333.277.599.61.58a48.1 48.1 0 005.427-.63 48.05 48.05 0 00.582-4.717.532.532 0 00-.533-.57v0c-.355 0-.676.186-.959.401-.29.221-.634.349-1.003.349-1.035 0-1.875-1.007-1.875-2.25s.84-2.25 1.875-2.25c.37 0 .713.128 1.003.349.283.215.604.401.96.401v0a.656.656 0 00.658-.663 48.422 48.422 0 00-.37-5.36c-1.886.342-3.81.574-5.766.689a.578.578 0 01-.61-.58v0z" />
                              </svg>              
                              Modules
                            </a>
        
                            <a href="#" class="text-blue-100 hover:text-white hover:bg-blue-600 group flex items-center px-2 py-2 text-sm leading-6 font-medium rounded-md">
                              <svg class="mr-4 h-6 w-6 flex-shrink-0 text-blue-200" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75a4.5 4.5 0 01-4.884 4.484c-1.076-.091-2.264.071-2.95.904l-7.152 8.684a2.548 2.548 0 11-3.586-3.586l8.684-7.152c.833-.686.995-1.874.904-2.95a4.5 4.5 0 016.336-4.486l-3.276 3.276a3.004 3.004 0 002.25 2.25l3.276-3.276c.256.565.398 1.192.398 1.852z" />
                                <path stroke-linecap="round" stroke-linejoin="round" d="M4.867 19.125h.008v.008h-.008v-.008z" />
                              </svg>              
                              Configuration
                            </a>
                        </div>
                        <div class="mt-6 pt-6">
                            <div class="space-y-1 px-2">
                                <router-link :to="{ name: 'about' }" active-class="bg-gray-800" class="group flex items-center rounded-md px-2 py-2 text-sm font-medium leading-6 text-blue-100 hover:bg-blue-600 hover:text-white">
                                  <svg class="mr-4 h-6 w-6 text-blue-200" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M18 18.72a9.094 9.094 0 003.741-.479 3 3 0 00-4.682-2.72m.94 3.198l.001.031c0 .225-.012.447-.037.666A11.944 11.944 0 0112 21c-2.17 0-4.207-.576-5.963-1.584A6.062 6.062 0 016 18.719m12 0a5.971 5.971 0 00-.941-3.197m0 0A5.995 5.995 0 0012 12.75a5.995 5.995 0 00-5.058 2.772m0 0a3 3 0 00-4.681 2.72 8.986 8.986 0 003.74.477m.94-3.197a5.971 5.971 0 00-.94 3.197M15 6.75a3 3 0 11-6 0 3 3 0 016 0zm6 3a2.25 2.25 0 11-4.5 0 2.25 2.25 0 014.5 0zm-13.5 0a2.25 2.25 0 11-4.5 0 2.25 2.25 0 014.5 0z" />
                                  </svg>                              
                                  About
                                </router-link>
        
                                <router-link :to="{ name: 'help' }" active-class="bg-gray-800" class="group flex items-center rounded-md px-2 py-2 text-sm font-medium leading-6 text-blue-100 hover:bg-blue-600 hover:text-white">
                                    <svg class="mr-4 h-6 w-6 text-blue-200" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M9.879 7.519c1.171-1.025 3.071-1.025 4.242 0 1.172 1.025 1.172 2.687 0 3.712-.203.179-.43.326-.67.442-.745.361-1.45.999-1.45 1.827v.75M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9 5.25h.008v.008H12v-.008z" />
                                  </svg> 
                                  Help
                                </router-link>
        
                            </div>
                        </div>
                    </nav>
                </div>
              </div>
              <div class="text-blue-500 text-right px-2">AIA Version: {{ version }}</div>
            </div>
        </div>
    
        <div class="flex flex-1 flex-col lg:pl-64">
          <div class="flex space-betweeen h-16 flex-shrink-0 border-b border-gray-200 bg-gray-100 lg:border-none px-4">
              <div class="flex items-center">
                <span :class="statusClass" class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium capitalize">{{ statusText }}</span>
              </div>
              <div class="flex flex-1 justify-end px-4 sm:px-6 w-100 lg:px-8">
                <div class="ml-4 flex items-center md:ml-6">
                    <button type="button" class="rounded-full bg-white p-1 text-gray-700 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
                      <span class="sr-only">View notifications</span>
                      <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                          <path stroke-linecap="round" stroke-linejoin="round" d="M14.857 17.082a23.848 23.848 0 005.454-1.31A8.967 8.967 0 0118 9.75v-.7V9A6 6 0 006 9v.75a8.967 8.967 0 01-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 01-5.714 0m5.714 0a3 3 0 11-5.714 0" />
                      </svg>
                    </button>
                </div>
                <div class="ml-4 flex items-center md:ml-6">
                  <button @click="displayExitModal = true;" type="button" class="rounded-full bg-white p-1 text-gray-700 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
                    <span class="sr-only">View notifications</span>
                    <svg class="w-6 h-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                      <path stroke-linecap="round" stroke-linejoin="round" d="M9 9.563C9 9.252 9.252 9 9.563 9h4.874c.311 0 .563.252.563.563v4.874c0 .311-.252.563-.563.563H9.564A.562.562 0 019 14.437V9.564z" />
                    </svg>
                  </button>
              </div>
              </div>
              <br>
          </div>
        </div>
    </div>
    <!-- Main content-->
    <div class="pl-64">
      <main class="flex-1 pb-8">
        <!-- Page header -->
        <div class="bg-white shadow">
            <div class="px-4 sm:px-6 lg:mx-auto lg:px-8">
                <div class="py-6 md:flex md:items-center md:justify-between">
                    <div class="min-w-0 flex-1">                  
                      <h1 class="text-2xl font-bold leading-7 text-gray-900 sm:truncate sm:leading-9">{{ $route.meta.title }}</h1>
                    </div>
                    <template v-if="$route.name != 'new-scan'">
                    <div class="mt-6 flex space-x-3 md:mt-0 md:ml-4">
                        <router-link :to="{ name: 'new-scan' }" class="inline-flex items-center rounded-md border border-transparent bg-blue-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">New Scan</router-link>
                    </div>
                    </template>
                </div>
            </div>
        </div>
        <div class="mx-auto px-4 sm:px-6 lg:px-8 mt-8">
          <router-view/>
        </div>
      </main>
    </div>
</template>

<script>
  export default {
    name: 'App',
    data() {
      return {
        status: 0,
        version: "0.0",
        displayExitModal: false,
        displayLeftModal: false
      }
    },
    mounted() {
      this.getToolData()
    },
    methods: {
      getToolData() {
        fetch('/api/data/tool-info')
          .then(response => response.json())
          .then(data => {
            console.log(data)
            this.status = data.status
            this.version = data.version
          })
      },
      stopTool(){
            this.axios.get('/api/stop-tool');
            this.displayExitModal = false;
            this.displayLeftModal = true;
      }
    },
    computed: {
      statusClass() {
        return {
          'bg-gray-700 text-white': this.status === 0,
          'bg-yellow-100 text-yellow-800': this.status === 1,
          'bg-blue-100 bg-green-800': this.status === 2
        }
      },
      statusText() {
        if(this.status == 0)
          return 'Waiting for scan'
        else if(this.status == 1)
          return 'Scanning'
        else if(this.status == 2)
          return 'Scan finished'
        else if(this.status == 3)
          return 'Shutdown'
      }
    }
  }
</script>