const {gql} = require('apollo-server-express');

module.exports = gql`

 type Series {
     id: Int!
     seriesName: String!
     idPatient: Int!
     idStudy: Int!
     idModality: Int!
     files: [File!]
     createdAt: String
     updatedAt: String
 }

extend type Query {
    getAllSeries: [Series!]
    getSingleSeries(id: Int!): Series
}

 extend type Mutation {
     createSeries(seriesName: String!, idPatient: Int!, idStudy: Int!, idModality: Int!): CreateSeriesResponse
     editSeries(id: Int!, seriesName: String!): [Int]
 }

 type CreateSeriesResponse {
    id: Int!
    seriesName: String!
    idPatient: Int!
    idStudy: Int!
    idModality: Int!
    createdAt: String!
 }

`;