const {gql} = require('apollo-server-express');

module.exports = gql`

 type Series {
     idSeries: Int!
     seriesName: String!
     patient: Patient!
     study: Study!
     modality: Modality!
     files: [File!]
     createdAt: String
     updatedAt: String
 }

extend type Query {
    getAllSeries: [Series!]
    getSingleSeries(idSeries: Int!): Series
}

 extend type Mutation {
     createSeries(seriesName: String!): CreateSeriesResponse
 }

 type CreateSeriesResponse {
    idSeries: Int!
    seriesName: String!
    createdAt: String!
 }

`;