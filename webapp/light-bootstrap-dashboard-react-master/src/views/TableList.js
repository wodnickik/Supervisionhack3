import React, { useState, useEffect, useMemo } from "react";


// react-bootstrap components
import {
  Badge,
  Button,
  Card,
  Navbar,
  Nav,
  Table,
  Container,
  Row,
  Col,
} from "react-bootstrap";

function TableList(props) {
  const allOffers = props.allOffers;
  return (
    <>
      <Container fluid>
        <Row>
          <Col md="13">
            <Card className="strpied-tabled-with-hover">
              <Card.Header>
                <Card.Title as="h4">Tabela oprocentowania</Card.Title>
                <p className="card-category">
                  Z uwzględnieniem alarmujących oferty, zaznaczonych na czerwono.
                </p>
              </Card.Header>
              <Card.Body className="table-full-width table-responsive px-0">
                <Table className="table-hover table-striped">
                  <thead>
                    <tr>
                      <th className="border-0">Bank</th>
                      <th className="border-0">Nazwa Oferty</th>
                      <th className="border-0">Oprocentowanie</th>
                      <th className="border-0">Typ oferty</th>
                      <th className="border-0">Długość (miesiące)</th>
                      <th className="border-0">Typ klienta</th>
                      <th className="border-0">Rodzaj oferty</th>
                      <th className="border-0">Minimalne środki</th>
                      <th className="border-0">Maksymalne środki</th>
                      <th className="border-0">Waluta</th>
                      <th className="border-0">Uwagi</th>
                      <th className="border-0">Ważne od</th>
                    </tr>
                  </thead>
                  <tbody>
                  {allOffers.length > 0 ? (
                  <React.Fragment>
                    {allOffers.map((offer, index) => (
                      <tr key={index} className={offer.dangerous_indicator ? 'text-danger' : ''}>
                      <td>{offer.bank_name}</td>
                      <td>{offer.offer_name}</td>
                      <td>{offer.interest}</td>
                      <td>{offer.offer_type}</td>
                      <td>{offer.offer_length_months}</td>
                      <td>{offer.client_type}</td>
                      <td>{offer.offer_kind}</td>
                      <td>{offer.min_resources}</td>
                      <td>{offer.max_resources}</td>
                      <td>{offer.currency}</td>
                      <td>{offer.additional_info}</td>
                      <td>{offer.valid_from_date}</td>
                    </tr>
                      ))} </React.Fragment> )
                      : ( <tr>
                        <td>No data</td>
                        <td>No data</td>
                        <td>No data</td>
                        <td>No data</td>
                        <td>No data</td>
                        <td>No data</td>
                        <td>No data</td>
                        <td>No data</td>
                        <td>No data</td>
                        <td>No data</td>
                        <td>No data</td>
                        <td>No data</td>
                      </tr>)}
                  </tbody>
                </Table>
              </Card.Body>
            </Card>
          </Col>
          <Col md="12">
            <Card className="card-plain table-plain-bg">
              <Card.Header>
                <Card.Title as="h4">Table on Plain Background</Card.Title>
                <p className="card-category">
                  Here is a subtitle for this table
                </p>
              </Card.Header>
              <Card.Body className="table-full-width table-responsive px-0">
                <Table className="table-hover">
                  <thead>
                    <tr>
                      <th className="border-0">ID</th>
                      <th className="border-0">Name</th>
                      <th className="border-0">Salary</th>
                      <th className="border-0">Country</th>
                      <th className="border-0">City</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>1</td>
                      <td>Dakota Rice</td>
                      <td>$36,738</td>
                      <td>Niger</td>
                      <td>Oud-Turnhout</td>
                    </tr>
                    <tr>
                      <td>2</td>
                      <td>Minerva Hooper</td>
                      <td>$23,789</td>
                      <td>Curaçao</td>
                      <td>Sinaai-Waas</td>
                    </tr>
                    <tr>
                      <td>3</td>
                      <td>Sage Rodriguez</td>
                      <td>$56,142</td>
                      <td>Netherlands</td>
                      <td>Baileux</td>
                    </tr>
                    <tr>
                      <td>4</td>
                      <td>Philip Chaney</td>
                      <td>$38,735</td>
                      <td>Korea, South</td>
                      <td>Overland Park</td>
                    </tr>
                    <tr>
                      <td>5</td>
                      <td>Doris Greene</td>
                      <td>$63,542</td>
                      <td>Malawi</td>
                      <td>Feldkirchen in Kärnten</td>
                    </tr>
                    <tr>
                      <td>6</td>
                      <td>Mason Porter</td>
                      <td>$78,615</td>
                      <td>Chile</td>
                      <td>Gloucester</td>
                    </tr>
                  </tbody>
                </Table>
              </Card.Body>
            </Card>
          </Col>
        </Row>
      </Container>
    </>
  );
}

export default TableList;
