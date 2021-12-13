const {gql} = require('apollo-server-express');

module.exports = gql`

 type File {
     idFile: Int!
     filePath: String!
     patient: Patient!
     study: Study!
     series: Series!
     createdAt: String
     updatedAt: String
 }

extend type Query {
    getAllFiles: [File!]
    getSingleFile(idFile: Int!): File
}

 extend type Mutation {
     createFile(filePath: String!): CreateFileResponse
 }

 type CreateFileResponse {
    idFile: Int!
    filePath: String!
    createdAt: String!
 }

`;