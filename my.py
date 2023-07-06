def match(j,c):
    return [i for i in c if (not i['desires_equity'] or i['desires_equity'] and j['equity_max']) and (i['current_location'] in j['locations'] or len([k for k in i['desired_locations'] if k in j['locations']]))]

print(match({ 'equity_max': 0, 'locations': ['Los Angeles', 'New York'] },[{
  'desires_equity': True, 
  'current_location': 'New York',
  'desired_locations': ['San Francisco', 'Los Angeles']
}, {
  'desires_equity': False, 
  'current_location': 'San Francisco',
  'desired_locations': ['Kentucky', 'New Mexico'] 
}]))
print(match({ 'equity_max': 1.2, 'locations': ['New York', 'Kentucky'] },[{
  'desires_equity': True, 
  'current_location': 'New York',
  'desired_locations': ['San Francisco', 'Los Angeles']
}, {
  'desires_equity': False, 
  'current_location': 'San Francisco',
  'desired_locations': ['Kentucky', 'New Mexico'] 
}]))