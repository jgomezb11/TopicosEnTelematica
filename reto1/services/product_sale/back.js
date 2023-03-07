const dotenv = require('dotenv')
const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');
const fs = require('fs');


dotenv.config({path: '../../config.env'})

const INVENTARY_IP = process.env.INVENTARY_IP;
const SALES_IP = process.env.SALES_IP;
const PROTO_PATH = process.env.PROTO_PATH;

const packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
    });

const productInventary = grpc.loadPackageDefinition(packageDefinition).ProductInventary;
const service = grpc.loadPackageDefinition(packageDefinition);

function SellProduct(call, callback){
  console.log("Processing a sale request for " + call.request.name_product)
  const productName = call.request.name_product;
  const client = new productInventary(INVENTARY_IP,grpc.credentials.createInsecure());

  client.ProductExist({name_product: productName} , (err, data) => {
    if(err){
      console.log(err);
    } else {
      var status = 1;
      if (data.product_id == -1){
        console.log('Can\'t make the sale because the product doesn\'t exists.')
        status = 2;
      }else{
        const data = call.request.name_product + ' sold.\n';
        fs.appendFile('sales_db.txt', data, (err) => {
            if (err) throw err;
            console.log('Data appended to file!');
        });
      }
      callback(null, {status_code: status})
    }
   });
};

function main() {
    const server = new grpc.Server();
    server.addService(service.ProductSale.service, {SellProduct:SellProduct});
    server.bindAsync(
        SALES_IP,
        grpc.ServerCredentials.createInsecure(),
        (error, port) => {
          console.log("Server running");
          server.start();
        }
      );
  }

main();
