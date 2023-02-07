<template>
  <Steps :currentStep="currentStep" />
  <Navigation :scanType="scanType" :currentStep="currentStep" @nextStep="nextStep" @prevStep="prevStep" />
  <Step1 v-if="currentStep === 1" @setScanType="setScanType"/>
  <Step2 v-if="currentStep === 2" :target="target" :targetType="targetType" :modules="modules"/>
  <Step3 v-if="currentStep === 3"/>

</template>

<script>
  import Navigation from '../components/NewScan/Navigation.vue'
  import Steps from '../components/NewScan/Steps.vue'
  import Step1 from '../components/NewScan/Step1.vue'
  import Step2 from '../components/NewScan/Step2.vue'
  import Step3 from '../components/NewScan/Step3.vue'
  export default {
    components: {
      Navigation,
      Steps,
      Step1,
      Step2,
      Step3
    },
    data() {
      return {
        currentStep: 1,
        target: "",
        targetType: 1,
        modules: [],
        scanType: 0
      }
    },
    methods: {
      nextStep() {
        this.currentStep++;
      },
      prevStep() {
        this.currentStep--;
      },
      setScanType(type) {
        if(type == 1 || type == 2) return;
        this.scanType = type;
        this.nextStep();
      }
    }
  }
</script>

