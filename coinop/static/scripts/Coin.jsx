class Coin extends React.Component {
    render() {
        const coin = this.props;
        return (
            <div className="list-group-item">
                <h3>{ coin.name }</h3>
                <p>Today: { coin.open } | { coin.close }</p>
                <p>Value: { coin.low } - { coin.high }</p>
                <p>Volume: { coin.volume }</p>
            </div>
        )
    }
}
