export default (item: Items) => {
    item.description = `新鲜程度:${item.fresh_level} 保质期至:${item.period}`
    return item.description
}