'use strict';
module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.createTable('Series', {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER
      },
      idStudy: {
        type: Sequelize.INTEGER,
        references: {
          model: {
            tableName: 'Studies',
          },
          key: 'id',
        },
      },
      idPatient: {
        type: Sequelize.INTEGER,
        references: {
          model: {
            tableName: 'Patients',
          },
          key: 'id',
        },
      },
      idModality: {
        type: Sequelize.INTEGER,
        references: {
          model: {
            tableName: 'Modalities',
          },
          key: 'id',
        },
      },
      seriesName: {
        type: Sequelize.STRING
      },
      createdAt: {
        allowNull: false,
        type: Sequelize.DATE
      },
      updatedAt: {
        allowNull: false,
        type: Sequelize.DATE
      }
    });
  },
  down: async (queryInterface, Sequelize) => {
    await queryInterface.dropTable('Series');
  }
};