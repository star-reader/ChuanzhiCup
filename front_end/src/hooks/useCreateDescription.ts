export default (item: Items) => {
    item.description = `新鲜度:${item.fresh_level} 保质期:${item.period}`
    return item.description
}