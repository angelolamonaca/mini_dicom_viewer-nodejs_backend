const {gql} = require('apollo-server-express');

module.exports = gql`

 type File {
     id: Int!
     filePath: String!
     patient: Patient!
     study: Study!
     series: Series!
     createdAt: String
     updatedAt: String
 }

extend type Query {
    getAllFiles: [File!]
    getSingleFile(id: Int!, idPatient: Int!, idStudy: Int!, idSeries: Int!): File
}

 extend type Mutation {
     createFile(filePath: String!): CreateFileResponse
 }

 type CreateFileResponse {
    id: Int!
    filePath: String!
    createdAt: String!
 }

`;