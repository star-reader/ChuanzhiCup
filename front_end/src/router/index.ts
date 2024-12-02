import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ConsumerDistributor from '../layout/ConsumerDistributor.vue'
import CustomerLogin from '../layout/CustomerLogin.vue'
import DistributorLogin from '../layout/DistributorLogin.vue'
import ProductList from '../components/ProductManagement/ProductList.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/login',
    name: 'Login',
    component: ConsumerDistributor,
  },
  {
    path: '/customer-login',
    name: 'CustomerLogin',
    component: CustomerLogin,
  },
  {
    path: '/distributor-login',
    name: 'DistributorLogin',
    component: DistributorLogin,
  },
  {
    path: '/product-list',
    name: 'ProductList',
    component: ProductList,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
