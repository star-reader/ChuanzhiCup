import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/',
    name: 'home',
    component: () => import('../views/HomeView.vue'),
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../layout/ConsumerDistributor.vue'),
  },
  {
    path: '/customer-login',
    name: 'CustomerLogin',
    component: () => import('../layout/CustomerLogin.vue'),
  },
  {
    path: '/distributor-login',
    name: 'DistributorLogin',
    component: () => import('../layout/DistributorLogin.vue'),
  },
  {
    path: '/manage-index',
    name: 'ManageIndex',
    component: () => import('../components/ProductManagement/ManageIndex.vue'),
  },
  {
    path: '/product-form',
    name: 'ProductForm',
    component: () => import('../views/ProductsFormView.vue'),
  },
  {
    path: '/product-list',
    name: 'ProductList',
    component: () => import('../components/ProductInfo/ProductList.vue'),
  },
  {
    path: '/manage-product',
    name: 'ManageProduct',
    component: () => import('../components/ProductManagement/ManageProduct.vue'),
  },
  {
    path: '/order-list',
    name: 'OrderList',
    component: () => import('../views/OrderView.vue'),
  },
  {
    path: '/customer-index',
    name: 'CustomerIndex',
    component: () => import('../components/Customer/CustomerIndex.vue'),
  },
  {
    path: '/statistics',
    name: 'Statistics',
    component: () => import('../components/Statistics/StatisticsView.vue'),
  }
]
const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
