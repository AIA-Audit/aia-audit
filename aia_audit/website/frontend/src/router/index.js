import { createRouter, createWebHistory } from "vue-router";
import AboutView from "../views/AboutView.vue";
import HelpView from "../views/HelpView.vue";
import HomeView from "../views/HomeView.vue";
import ScanView from "../views/ScanView.vue";
import MyScansView from "../views/MyScansView.vue";
import ModulesView from "../views/ModulesView.vue";
import NewScanView from "../views/NewScanView.vue";
import SettingsView from "../views/SettingsView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    /* User Routes */
    {
      path: "/",
      name: "home",
      component: HomeView,
      meta: { title: 'Dashboard' },
    },
    {
      path: "/new/scan",
      name: "new-scan",
      component: NewScanView,
      meta: { title: 'New Scan' },
    },
    {
      path: "/scan/:id",
      name: "scan",
      component: ScanView,
      meta: { title: 'Scan results' },
    },
    {
      path: "/scans",
      name: "scans",
      component: MyScansView,
      meta: { title: 'My Scans' },
    },
    {
      path: "/modules",
      name: "modules",
      component: ModulesView,
      meta: { title: 'Modules' },
    },
    {
      path: "/about",
      name: "about",
      component: AboutView,
      meta: { title: 'About' },
    },
    {
      path: "/help",
      name: "help",
      component: HelpView,
      meta: { title: 'Help' },
    },
    {
      path: "/settings",
      name: "settings",
      component: SettingsView,
      meta: { title: 'Settings', ignore_setup: true },
    },
  ],
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title;
  next();
});

export default router;
