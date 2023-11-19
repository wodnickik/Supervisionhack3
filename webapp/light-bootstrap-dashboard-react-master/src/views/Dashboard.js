import React, {useEffect, useState} from "react";
import ChartistGraph from "react-chartist";
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
  Form,
  OverlayTrigger,
  Tooltip,
} from "react-bootstrap";

function Dashboard() {
   let [plotValues, setPlotValues] = useState([]);
  useEffect(() => {
    getPlotValues();
  }, []);

  let getPlotValues = async () => {
    let response = await fetch("http://127.0.0.1:8000/get_plot_values");
    let data = await response.json();
    setPlotValues(data);
  };

  return (

    <>
      <Container fluid>
        <Row>+
        </Row>
        <Row>
          <Col md="12">
            <Card>
              <Card.Header>
                <Card.Title as="h4">Stopy procentowe</Card.Title>
                <p className="card-category">Na przestrzeni lat</p>
              </Card.Header>
              <Card.Body>
                <div className="ct-chart" id="chartHours">
                  <ChartistGraph
                    data={{
                      labels: [
                          plotValues["Random Bank Polski "][0]
                      ],
                      series: [
                        plotValues["Awesome Bank Polski "][1].slice(7),
                        plotValues["Gold Bank Polski "][1].slice(5),
                        plotValues["Random Bank Polski "][1],
                          ],
                    }}
                    type="Line"
                    options={{
                      low: -0.025,
                      high: 0.1,
                      showArea: false,
                      height: "245px",
                      axisX: {
                        showGrid: false,
                      },
                      lineSmooth: true,
                      showLine: true,
                      showPoint: true,
                      fullWidth: true,
                      chartPadding: {
                        right: 50,
                      },
                    }}
                    responsiveOptions={[
                      [
                        "screen and (max-width: 640px)",
                        {
                          axisX: {
                            labelInterpolationFnc: function (value) {
                              return value[0];
                            },
                          },
                        },
                      ],
                    ]}
                  />
                </div>
              </Card.Body>
            </Card>
          </Col>
        </Row>
        <Row>
        </Row>
      </Container>
    </>
  );
}

export default Dashboard;
