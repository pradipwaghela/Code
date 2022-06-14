<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
    <meta name="description" content="">
    <meta name="author" content="">
    <title>Vesta Hotels</title>
</head>
<script>
function Validate(data){

    var hotel = $(':selected',data.hotel_name).val();
    var url="https://live.ipms247.com/booking/book-rooms-"+hotel;
    alert (url)
    data.action = url;
    
    return true;
}
</script>
<body>
<form onsubmit="return Validate(this)" action="" method="post">
<select name="hotel_name" id="">
        <option value="vestainternational">Vesta International</option>
        <option value="vestamauryapalace">Bikaner Palce</option>
        <option value="vestabikanerpalace">Bikaner Palce</option>
    </select>
    <input type="submit" value="submit"></button> 
</form>
</body>
</html>